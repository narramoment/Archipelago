import json
import logging
import queue
import time
import struct
import random
from dataclasses import dataclass
from queue import Queue
from typing import Callable

from PyMemoryEditor import OpenProcess, PyMemoryEditorError

import asyncio
from asyncio import StreamReader, StreamWriter, Lock

from NetUtils import NetworkItem
from ..items import item_table, Jak2ItemData, TRAP_ID_START, TRAP_ID_END, ITEM_ID_FILLER_START, ITEM_ID_FILLER_END
from ..game_id import jak2_gk, jak2_goalc

logger = logging.getLogger("Jak2ReplClient")


@dataclass
class JsonMessageData:
    my_item_name: str | None = None
    my_item_finder: str | None = None
    their_item_name: str | None = None
    their_item_owner: str | None = None


ALLOWED_CHARACTERS = frozenset(
    {
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        " ", "!", ":", ",", ".", "/", "?", "-", "=", "+", "'", "(", ")", '"',
    }
)


class Jak2ReplClient:
    ip: str
    port: int
    reader: StreamReader
    writer: StreamWriter
    lock: Lock
    connected: bool = False
    initiated_connect: bool = False
    received_deathlink: bool = False

    initial_item_count = -1
    received_initial_items = False
    processed_initial_items = False

    # Variables to handle waiting for compilation to finish without blocking the event loop.
    waiting_for_compile: bool = False
    compile_ready_time: float = 0.0

    # The REPL client needs the REPL/compiler process running, but that process
    # also needs the game running. Therefore, the REPL client needs both running.
    gk_process: OpenProcess | None = None
    goalc_process: OpenProcess | None = None

    item_inbox: dict[int, NetworkItem] = {}
    inbox_index = 0
    json_message_queue: Queue[JsonMessageData] = queue.Queue()

    slot_seed: str = ""

    # Logging callbacks
    # These will write to the provided logger, as well as the Client GUI with color markup.
    log_error: Callable  # Red
    log_warn: Callable  # Orange
    log_success: Callable  # Green
    log_info: Callable     # White (default)

    def __init__(self,
                 log_error_callback: Callable,
                 log_warn_callback: Callable,
                 log_success_callback: Callable,
                 log_info_callback: Callable,
                 memr,
                 ip: str = "127.0.0.1",
                 port: int = 8181):
        self.ip = ip
        self.port = port
        self.lock = asyncio.Lock()
        self.log_error = log_error_callback
        self.log_warn = log_warn_callback
        self.log_success = log_success_callback
        self.log_info = log_info_callback
        self.memr = memr

    async def main_tick(self):
        if self.initiated_connect:
            await self.connect()
            self.initiated_connect = False

        if self.connected:
            try:
                OpenProcess(name=jak2_gk)
            except PyMemoryEditorError as e:
                msg = (
                    f"Error reading game memory! (Did the game crash?)\n"
                    f"Please close all open windows and reopen the Jak II Client "
                    f"from the Archipelago Launcher.\n"
                    f"If the game and compiler do not restart automatically, please follow these steps:\n"
                    f"   Run the OpenGOAL Launcher, click Jak II > Features > Mods > ArchipelaGOAL.\n"
                    f"   Then click Advanced > Play in Debug Mode.\n"
                    f"   Then click Advanced > Open REPL.\n"
                    f"   Then close and reopen the Jak II Client from the Archipelago Launcher."
                )
                self.log_error(logger, msg)
                logger.error(e)
                self.connected = False
            try:
                # Ping to see if it's alive.
                OpenProcess(name=jak2_goalc)
            except PyMemoryEditorError as e:
                msg = (
                    f"Error sending data to compiler! (Did the compiler crash?)\n"
                    f"Please close all open windows and reopen the Jak II Client "
                    f"from the Archipelago Launcher.\n"
                    f"If the game and compiler do not restart automatically, please follow these steps:\n"
                    f"   Run the OpenGOAL Launcher, click Jak II > Features > Mods > ArchipelaGOAL.\n"
                    f"   Then click Advanced > Play in Debug Mode.\n"
                    f"   Then click Advanced > Open REPL.\n"
                    f"   Then close and reopen the Jak II Client from the Archipelago Launcher."
                )
                self.log_error(logger, msg)
                logger.error(e)
                self.connected = False
        else:
            return

        # When connecting the game to the AP server on the title screen, we may be processing items from starting
        # inventory or items received in an async game. Once we have caught up to the initial count, tell the player
        # that we are ready to start. New items may even come in during the title screen, so if we go over the count,
        # we should still send the ready signal.
        if not self.processed_initial_items:
            if self.inbox_index >= self.initial_item_count >= 0:
                self.processed_initial_items = True
                await self.send_connection_status("ready")

        # Receive Items from AP. Handle 1 item per tick.
        if len(self.item_inbox) > self.inbox_index:
            await self.receive_item()
            await self.save_data()
            self.inbox_index += 1

        if self.received_deathlink:
            await self.receive_deathlink()
            self.received_deathlink = False

        # Progressively empty the queue during each tick
        # if text messages happen to be too slow we could pool dequeuing here,
        # but it'd slow down the ItemReceived message during release
        if not self.json_message_queue.empty():
            json_txt_data = self.json_message_queue.get_nowait()
            await self.write_game_text(json_txt_data)

    async def send_form(self, form: str, print_ok: bool = True) -> bool:
        header = struct.pack("<II", len(form), 10)
        async with self.lock:
            self.writer.write(header + form.encode())
            await self.writer.drain()

            try:
                response_data = await asyncio.wait_for(self.reader.read(1024), timeout=120.0)
                response = response_data.decode()
            except asyncio.TimeoutError:
                self.log_error(logger, f"Timed out while waiting for REPL response to {form}")
                return False

            if response and len(response.strip()) > 0:
                if print_ok:
                    logger.debug(response)
                return True
            else:
                self.log_error(logger, f"Unexpected response from REPL: {response}")
                return False

    async def connect(self):
        try:
            self.gk_process = OpenProcess(name=jak2_gk)
            logger.debug("Found the gk process: " + str(self.gk_process.pid))
        except PyMemoryEditorError as e:
            self.log_error(logger, "Could not find the game process.")
            logger.error(e)
            return

        try:
            self.goalc_process = OpenProcess(name=jak2_goalc)
            logger.debug("Found the goalc process: " + str(self.goalc_process.pid))
        except PyMemoryEditorError as e:
            self.log_error(logger, "Could not find the compiler process.")
            logger.error(e)
            return

        try:
            self.reader, self.writer = await asyncio.open_connection(self.ip, self.port)
            await asyncio.sleep(1)
            connect_data = await self.reader.read(1024)
            welcome_message = connect_data.decode()

            # Should be the OpenGOAL welcome message (ignore version number).
            if "Connected to OpenGOAL" and "nREPL!" in welcome_message:
                logger.debug(welcome_message)
            else:
                self.log_error(
                    logger, f'Unable to connect to REPL websocket: unexpected welcome message "{welcome_message}"'
                )
        except ConnectionRefusedError as e:
            self.log_error(logger, f"Unable to connect to REPL websocket: {e.strerror}")
            return

        if self.reader and self.writer:
            self.log_info(logger, "[1/5] Listen on the game's port...")
            await asyncio.sleep(0.5)
            await self.send_form("(lt)", print_ok=False)
            await asyncio.sleep(3)

            self.log_info(logger, "[2/5] Set debug flag to on...")
            await asyncio.sleep(0.5)
            await self.send_form("(set! *debug-segment* #t)", print_ok=False)

            self.log_info(logger, "[3/5] Compile the game...")
            await asyncio.sleep(0.5)
            await self.send_form("(mi)", print_ok=False)

            self.log_info(logger, "[4/5] Set cheat mode to off...")
            await asyncio.sleep(0.5)
            await self.send_form("(set! *cheat-mode* #f)", print_ok=False)
            await asyncio.sleep(0.5)
            self.log_info(logger, "[5/5] Run the title screen...")
            await self.send_form("(start 'play (get-continue-by-name *game-info* \"title-start\"))")
            self.log_success(logger, "The REPL is ready!")
            self.connected = True

    async def print_status(self):
        gc_proc_id = str(self.goalc_process.pid) if self.goalc_process else "None"
        gk_proc_id = str(self.gk_process.pid) if self.gk_process else "None"
        msg = f"REPL Status:\n" f"   REPL process ID: {gc_proc_id}\n" f"   Game process ID: {gk_proc_id}\n"
        try:
            if self.reader and self.writer:
                addr = self.writer.get_extra_info("peername")
                addr = str(addr) if addr else "None"
                msg += f"   Game websocket: {addr}\n"
        except ConnectionResetError:
            msg += f"   Connection to the game was lost or reset!"
        last_item = str(getattr(self.item_inbox[self.inbox_index], "item")) if (self.inbox_index
                                                                                and self.inbox_index <
                                                                                len(self.item_inbox)) else "None"
        msg += f"   Last item received: {last_item}\n"
        self.log_info(logger, msg)

    # To properly display in-game text:
    # - It must be a valid character from the ALLOWED_CHARACTERS list.
    # - All lowercase letters must be uppercase.
    # - It must be wrapped in double quotes (for the REPL command).
    # - Apostrophes must be handled specially - GOAL uses invisible ASCII character 0x12.
    # I also only allotted 32 bytes to each string in OpenGOAL, so we must truncate.
    @staticmethod
    def sanitize_game_text(text: str) -> str:
        result = "".join([c if c in ALLOWED_CHARACTERS else "?" for c in text[:32]]).upper()
        result = result.replace("'", "\\c12")
        return f'"{result}"'

    # Like sanitize_game_text, but the settings file will NOT allow any whitespace in the slot_name or slot_seed data.
    # And don't replace any chars with "?" for good measure.
    @staticmethod
    def sanitize_file_text(text: str) -> str:
        allowed_chars_no_extras = ALLOWED_CHARACTERS - {" ", "'", "(", ")", '"'}
        result = "".join([c if c in allowed_chars_no_extras else "" for c in text[:16]]).upper()
        return f'"{result}"'

    # Pushes a JsonMessageData object to the json message queue to be processed during the repl main_tick
    def queue_game_text(self, my_item_name, my_item_finder, their_item_name, their_item_owner):
        self.json_message_queue.put(JsonMessageData(my_item_name, my_item_finder, their_item_name, their_item_owner))

    # OpenGOAL can handle both its own string datatype and C-like character pointers (charp).
    async def write_game_text(self, data: JsonMessageData):
        logger.debug(f"Sending info to the in-game messenger!")
        body = ""
        if data.my_item_name and data.my_item_finder:
            is_trap = "Trap" in data.my_item_name
            is_filler = any(f in data.my_item_name for f in ("Pill", "Ammo", "Health Pack"))
            if is_trap and data.my_item_finder != "MYSELF":
                direction = "'trap"
            elif data.my_item_finder == "MYSELF":
                direction = "'found"
            else:
                direction = "'recv"
            body += (f" (let ((m (the ap-messenger (process-by-name \"ap-messenger\" *active-pool*)))) "
                     f" (when m (append-messages m {direction} "
                     f" {self.sanitize_game_text(data.my_item_name)} "
                     f" {self.sanitize_game_text(data.my_item_finder)}"
                     f" {'#t' if is_filler else '#f'})))")
        if data.their_item_name and data.their_item_owner:
            is_filler_theirs = any(f in data.their_item_name for f in ("Pill", "Ammo", "Health Pack"))
            if data.their_item_owner == "MYSELF":
                direction = "'found"
            else:
                direction = "'sent"
            body += (f" (let ((m (the ap-messenger (process-by-name \"ap-messenger\" *active-pool*)))) "
                     f" (when m (append-messages m {direction} "
                     f" {self.sanitize_game_text(data.their_item_name)} "
                     f" {self.sanitize_game_text(data.their_item_owner)}"
                     f" {'#t' if is_filler_theirs else '#f'})))")
        await self.send_form(f"(begin {body} (none))", print_ok=False)

    async def receive_item(self):
        item = getattr(self.item_inbox[self.inbox_index], "item")

        # Unknown item check
        if item not in item_table:
            self.log_error(logger, f"Tried to receive item with unknown AP ID {item}!")
            return False

        item_data: Jak2ItemData = item_table[item]
        item_name: str = item_data.name
        item_symbol: str = item_data.symbol


        # Trap handling
        if TRAP_ID_START <= item <= TRAP_ID_END:
            ok = await self.send_form(f"(ap-trap-received! '{item_symbol})", print_ok=False)
            if ok:
                logger.debug(f"Received {item_name}!")
            else:
                self.log_error(logger, f"Unable to receive {item_name}!")
            return ok

        # Normal item handling
        ok = await self.send_form(f"(ap-item-received! '{item_symbol})", print_ok=False)
        if ok:
            logger.debug(f"Received {item_name}!")
        else:
            self.log_error(logger, f"Unable to receive {item_name}!")

        return ok


    async def receive_deathlink(self) -> bool:

        # Because it should be funny sometimes, right?
        death_types = ["'death",
                      "'death",
                      "'death",
                      "'death",
                      "'endlessfall",
                      "'dark-eco-pool",
                      "'crush",
                      "'smush",
                      "'drown-death",
                      "'lava",
                      "'grenade",
                      "'explode",
                      "'big-explosion"]
        chosen_death = random.choice(death_types)

        ok = await self.send_form(f"(ap-deathlink-received! {chosen_death})", print_ok=False)
        if ok:
            logger.debug(f"Received deathlink signal!")
        else:
            self.log_error(logger, f"Unable to receive deathlink signal!")
        return ok

    # OpenGOAL has a limit of 8 parameters per function. We've already hit this limit. So, define a new datatype
    # in OpenGOAL that holds all these options, instantiate the type here, and have ap-setup-options! function take
    # that instance as input.
    async def setup_options(self,
                            slot_name: str,
                            slot_seed: str,
                            trap_time: int,
                            completion_type: int,
                            specific_mission_value: int,
                            mission_count_value: int,
                            randomize_oracle_cost: int,
                            oracle_cost_level0: int,
                            oracle_cost_level1: int,
                            oracle_cost_level2: int,
                            oracle_cost_level3: int,
                            minigame_medal_checks: int = 0,
                            orbsanity: int = 0,
                            orbs: int = 1) -> bool:
        sanitized_name = self.sanitize_file_text(slot_name)
        sanitized_seed = self.sanitize_file_text(slot_seed)

        ok = await self.send_form(f"(ap-setup-options! (new 'static 'ap-seed-options "
                                  f":slot-name {sanitized_name} "
                                  f":slot-seed {sanitized_seed} "
                                  f":trap-duration {trap_time}.0 "
                                  f":completion-type {completion_type} "
                                  f":completion-value {specific_mission_value} "
                                  f":completion-mission-count {mission_count_value} "
                                  f":randomize-oracle-cost {randomize_oracle_cost} "
                                  f":oracle-cost-level0 {oracle_cost_level0} "
                                  f":oracle-cost-level1 {oracle_cost_level1} "
                                  f":oracle-cost-level2 {oracle_cost_level2} "
                                  f":oracle-cost-level3 {oracle_cost_level3} "
                                  f":minigame-medal-checks {minigame_medal_checks} "
                                  f":orbsanity {orbsanity} "
                                  f":orbs {orbs} )) ", print_ok=False)
        message = (f"Setting options: \n"
                   f"   Slot Name {sanitized_name}, \n"
                   f"   Slot Seed {sanitized_seed}, \n"
                   f"   Trap Duration {trap_time}, \n"
                   f"   Goal Type {completion_type}, \n"
                   f"   Specific Value {specific_mission_value}, \n"
                   f"   Mission Count Value {mission_count_value}, \n"
                   f"   Randomize Oracle Cost {randomize_oracle_cost}, \n"
                   f"   Oracle Cost Level0 {oracle_cost_level0}, \n"
                   f"   Oracle Cost Level1 {oracle_cost_level1}, \n"
                   f"   Oracle Cost Level2 {oracle_cost_level2}, \n"
                   f"   Oracle Cost Level3 {oracle_cost_level3}, \n"
                   f"   Minigame Medal Checks {minigame_medal_checks}, \n"
                   f"   Orbsanity {orbsanity}, \n"
                   f"   Orbs {orbs}... ")
        if ok:
            logger.debug(message + "Success!")
        else:
            self.log_error(logger, message + "Failed!")
        return ok

    async def send_connection_status(self, status: str) -> bool:
        ok = await self.send_form(f"(ap-set-connection-status! (ap-connection-status {status}))", print_ok=False)
        if ok:
            logger.debug(f"Connection Status {status} set!")
        else:
            self.log_error(logger, f"Connection Status {status} failed to set!")
        return ok

    async def save_data(self):
        filename = f"jakii_item_inbox_{self.slot_seed}.json" if self.slot_seed else "jakii_item_inbox.json"
        with open(filename, "w+") as f:
            dump = {
                "inbox_index": self.inbox_index,
                "item_inbox": [
                    {
                        "item": self.item_inbox[k].item,
                        "location": self.item_inbox[k].location,
                        "player": self.item_inbox[k].player,
                        "flags": self.item_inbox[k].flags,
                    }
                    for k in self.item_inbox
                ],
            }
            json.dump(dump, f, indent=4)

    def load_data(self):
        self.inbox_index = 0
        self.item_inbox = {}