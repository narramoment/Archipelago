# Archipelago Imports
import math

import settings
from Options import OptionError, OptionGroup
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import components, Component, launch_subprocess, Type, icon_paths
from BaseClasses import (Tutorial, ItemClassification as ItemClass)
from typing import cast, ClassVar, Any

# Jak 2 imports
from . import options
from .game_id import jak2_name, jak2_max
from .items import (item_table, ITEM_ID_KEY_START, ITEM_ID_KEY_END, ITEM_ID_FILLER_START, ITEM_ID_FILLER_END,
                    TRAP_ID_START, TRAP_ID_END, ORBSANITY_ID, Jak2ItemData, Jak2Item, orb_item_table,
                    orb_to_id)
from .locs import (mission_locations)
from .locations import (JakIILocation, all_locations_table)
from .locs.mission_locations import Jak2MissionData, get_minigame_medal_locations, get_orb_locations, orb_names_table
from .regs.region_base import JakIIRegion
from worlds.jakii.rules import (slums_to_port, slums_to_stadium, slums_to_market, slums_to_landing, slums_to_nest,
                                any_gun)

TOTAL_ORBS = 286


class Jak2Settings(settings.Group):
    class RootDirectory(settings.UserFolderPath):
        """Path to folder containing the ArchipelaGOAL Jak 2 mod executables (gk.exe and goalc.exe).
        Ensure this path contains forward slashes (/) only. This setting only applies if
        Auto Detect Root Directory is set to false."""
        description = "ArchipelaGOAL Jak 2 Root Directory"

    class AutoDetectRootDirectory(settings.Bool):
        """Attempt to find the OpenGOAL installation and the Jak 2 mod executables (gk.exe and goalc.exe)
        automatically. If set to true, the ArchipelaGOAL Jak 2 Root Directory setting is ignored."""
        description = "ArchipelaGOAL Jak 2 Auto Detect Root Directory"

    root_directory: RootDirectory = "C:/Program Files/OpenGOAL/features/jak2/mods/archipelagoal/archipelagoal"
    auto_detect_root_directory: AutoDetectRootDirectory = True


def launch_client():
    from . import client
    launch_subprocess(client.launch, name="Jak2Client")


components.append(Component("Jak II Client",
                            func=launch_client,
                            component_type=Type.CLIENT,
                            icon="jak2_icon"))


icon_paths["jak2_icon"] = f"ap:{__name__}/icons/jak2_icon.png"


class JakIIWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up ArchipelaGOAL II (Archipelago on OpenGOAL)",
        "English",
        "setup_en.md",
        "setup/en",
        ["narramoment"]
    )

    tutorials = [setup_en]
    bug_report_page = "https://github.com/narramoment/Archipelago/issues"
    option_groups = [
        OptionGroup("Traps", [
            options.PercentOfFillerItemsReplacedWithTraps,
            options.TrapEffectDuration,
            options.TrapWeights
        ])
    ]


class JakIIWorld(World):
    """
    Jak II is an action-adventure game published by Naughty Dog in 2003 for the PlayStation 2.
    Set directly after the events of Jak and Daxter: The Precursor Legacy, Jak, Daxter, Samos
    and Keira have set up the Rift Rider they found at the end of their previous adventure, and
    are ready to see where it leads. However, a strange and hostile species of creatures known as
    Metal Heads suddenly fly through the portal, and in a panic, Daxter activates the machine,
    sending them flying through the open portal. Separated, they find themselves in "glorious" Haven City,
    and Jak is quickly captured. Two years later, Daxter finds Jak locked up in prison,
    and Jak has only one thought on his mind: vengeance.
    """

    game = jak2_name
    web = JakIIWebWorld()

    # Options
    options_dataclass = options.JakIIOptions
    options: options.JakIIOptions

    # Settings will be applied after class definition
    settings: ClassVar[Jak2Settings]

    item_name_to_id = {item_data.name: k for k, item_data in item_table.items()}
    location_name_to_id = {**{data.name: k for k, data in all_locations_table.items()},
                           **get_minigame_medal_locations(True), **get_orb_locations(True)}
    item_name_groups = {
        "Items": {item.name for item in item_table.values()}
    }
    location_name_groups = {}
    origin_region_name = "Mission Tree"

    # Cache option-related values.
    completion_type: int
    completion_value: int
    total_items: int = 56
    total_prog_items: int = 33
    total_filler_items: int = 0
    total_trap_items: int = 0
    trap_weights: tuple[list[str], list[int]]
    orb_item_table: str = ""
    orb_item_name: str = ""
    orb_item_id: int = 0

    def generate_early(self) -> None:
        # Cache completion conditions and values.
        self.completion_type = self.options.jak_2_completion_condition.value  # Sorry about the naming here.
        if self.completion_type == options.CompletionCondition.option_complete_specific_mission:
            self.completion_value = self.options.specific_mission_for_completion.value
        elif self.completion_type == options.CompletionCondition.option_complete_number_of_missions:
            self.completion_value = self.options.number_of_missions_for_completion.value
        else:
            raise OptionError(f"Unknown completion condition selected for Jak II: {self.completion_type}")

        if self.options.orbsanity:
            self.orb_item_name = orb_item_table[1]
            self.orb_item_id = orb_to_id[1]

        # Calculate Filler and Traps, if applicable
        available_slots = self.total_items - self.total_prog_items
        trap_replace_percent = self.options.percent_filler_replaced_with_traps / 100
        self.total_trap_items = math.floor(available_slots * trap_replace_percent)
        self.total_filler_items = available_slots - self.total_trap_items

        self.trap_weights = self.options.trap_weights.weighted_pair

    @staticmethod
    def item_data_helper(item: int) -> list[tuple[int, ItemClass, int]]:
        # count,num,classification
        data: list[tuple[int, ItemClass, int]] = []

        # Determine item classification based on ID ranges
        if ITEM_ID_KEY_START <= item <= ITEM_ID_KEY_END:
            # Key/progression items (IDs 1-33)
            data.append((1, ItemClass.progression | ItemClass.useful, 0))
        elif ITEM_ID_FILLER_START <= item <= ITEM_ID_FILLER_END:
            # Filler items (IDs 34-39) (will be made manually)
            data.append((0, ItemClass.filler, 0))
        elif TRAP_ID_START <= item <= TRAP_ID_END:
            # Trap Items (their own table) (will also be made manually)
            data.append((0, ItemClass.trap, 0))
        elif item in orb_to_id.values():
            # Orbs, count is determined dynamically in create_items(), not here
            data.append((1, ItemClass.useful, 0))
        else:
            # If we try to make items with ID's outside defined ranges, something has gone wrong
            raise KeyError(f"Tried to fill item pool with unknown ID {item}. Valid ranges: "
                           f"key items ({ITEM_ID_KEY_START}-{ITEM_ID_KEY_END}), "
                           f"filler items ({ITEM_ID_FILLER_START}-{ITEM_ID_FILLER_END})"
                           f"trap items ({TRAP_ID_START}-{TRAP_ID_END})")
        return data

    def create_items(self) -> None:
        items_made: int = 0
        for item_name in self.item_name_to_id:
            item_id = self.item_name_to_id[item_name]

            if ITEM_ID_FILLER_START <= item_id <= ITEM_ID_FILLER_END:
                continue
            if TRAP_ID_START <= item_id <= TRAP_ID_END:
                continue
            if item_id in orb_to_id.values():
                continue

            data = self.item_data_helper(item_id)
            for (count, classification, num) in data:
                self.multiworld.itempool += [
                    Jak2Item(item_name, classification, item_id, self.player)
                    for _ in range(count)]
                items_made += count

        if self.options.orbsanity:
            self.multiworld.itempool += [
                Jak2Item(self.orb_item_name, ItemClass.useful, self.orb_item_id, self.player)
                for _ in range(TOTAL_ORBS)
            ]
            items_made += TOTAL_ORBS

        # Handle Unfilled Locations!
        all_regions = self.multiworld.get_regions(self.player)
        total_locations = sum(reg.location_count for reg in cast(list[JakIIRegion], all_regions))
        total_filler = total_locations - items_made

        trap_percent = self.options.percent_filler_replaced_with_traps.value / 100
        trap_count = int(total_filler * trap_percent)
        filler_count = total_filler - trap_count

        trap_names, trap_weights = self.options.trap_weights.weighted_pair
        if all(w==0 for w in trap_weights):
            trap_count = 0
            filler_count = total_filler

            print(f"[JakII] total_locations={total_locations}, items_made={items_made}, total_filler={total_filler}")
            print(f"[JakII] trap_percent={trap_percent}, trap_count={trap_count}, filler_count={filler_count}")
            print(f"[JakII] trap_weights={list(zip(trap_names, trap_weights))}")
        self.multiworld.itempool += [self.create_filler() for _ in range(max(0,filler_count))]
        self.multiworld.itempool += [self.create_trap() for _ in range(max(0,trap_count))]

    def create_trap(self) -> Jak2Item:
        trap_names, trap_weights = self.options.trap_weights.weighted_pair
        trap_name = self.random.choices(trap_names, weights=trap_weights, k=1)[0]
        trap_id = self.item_name_to_id[trap_name]
        return Jak2Item(trap_name, ItemClass.trap, trap_id, self.player)

    def create_item(self, name: str) -> Jak2Item:
        item_id = self.item_name_to_id[name]

        _, classification, _ = self.item_data_helper(item_id)[0]
        return Jak2Item(name, classification, item_id, self.player)

    def get_filler_item_name(self) -> str:
        filler_item_names = ["Dark Eco Pill", "Health Pack", "Scatter Gun Ammo", "Blaster Ammo", "Vulcan Fury Ammo",
                             "Peacemaker Ammo"]
        return self.random.choice(filler_item_names)

    def create_regions(self) -> None:

        # Add missions to the mission tree.
        mission_tree_region = JakIIRegion("Mission Tree", self.player, self.multiworld)
        for mission_id in all_locations_table:
            mission = all_locations_table[mission_id]
            mission_tree_region.add_jak_mission(mission_id, mission.name, mission.rule)

        # Minigame bronze/silver/gold medal locations — only added when the option is enabled.
        if self.options.minigame_medal_checks:
            scatter_gun_mission = all_locations_table[7]
            blaster_gun_mission = all_locations_table[18]
            onin_mission = all_locations_table[39]
            jetboard_mission = all_locations_table[16]
            class3_mission = all_locations_table[35]
            class2_mission = all_locations_table[46]
            class1_mission = all_locations_table[54]
            reverse_class3_mission = all_locations_table[131]
            reverse_class2_mission = all_locations_table[132]
            reverse_class1_mission = all_locations_table[133]
            city_port_race_mission = all_locations_table[126]
            erol_race_mission = all_locations_table[125]

            medal_rules = {
                "Scatter Gun Course - Bronze Medal": scatter_gun_mission.rule,
                "Scatter Gun Course - Silver Medal": scatter_gun_mission.rule,
                "Scatter Gun Course - Gold Medal": scatter_gun_mission.rule,
                "Blaster Gun Course - Bronze Medal": blaster_gun_mission.rule,
                "Blaster Gun Course - Silver Medal": blaster_gun_mission.rule,
                "Blaster Gun Course - Gold Medal": blaster_gun_mission.rule,
                "Vulcan Fury Gun Course - Bronze Medal": lambda state, player: state.has("Vulcan Fury", player)
                                                                               and slums_to_port(state, player),
                "Vulcan Fury Gun Course - Silver Medal": lambda state, player: state.has("Vulcan Fury", player)
                                                                               and slums_to_port(state, player),
                "Vulcan Fury Gun Course - Gold Medal": lambda state, player: state.has("Vulcan Fury", player)
                                                                             and slums_to_port(state, player),
                "Peacemaker Gun Course - Bronze Medal": lambda state, player: state.has("Peacemaker", player)
                                                                              and slums_to_port(state, player),
                "Peacemaker Gun Course - Silver Medal": lambda state, player: state.has("Peacemaker", player)
                                                                              and slums_to_port(state, player),
                "Peacemaker Gun Course - Gold Medal": lambda state, player: state.has("Peacemaker", player)
                                                                            and slums_to_port(state, player),
                "Onin's Game - Medal": onin_mission.rule,
                "JET-Board Challenge - Bronze Medal": jetboard_mission.rule,
                "JET-Board Challenge - Silver Medal": jetboard_mission.rule,
                "JET-Board Challenge - Gold Medal": jetboard_mission.rule,
                "Class 3 Race - Bronze Medal": class3_mission.rule,
                "Class 3 Race - Silver Medal": class3_mission.rule,
                "Class 3 Race - Gold Medal": class3_mission.rule,
                "Class 2 Race - Bronze Medal": class2_mission.rule,
                "Class 2 Race - Silver Medal": class2_mission.rule,
                "Class 2 Race - Gold Medal": class2_mission.rule,
                "Class 1 Race - Bronze Medal": class1_mission.rule,
                "Class 1 Race - Silver Medal": class1_mission.rule,
                "Class 1 Race - Gold Medal": class1_mission.rule,
                "Reverse Class 3 Race - Bronze Medal": reverse_class3_mission.rule,
                "Reverse Class 3 Race - Silver Medal": reverse_class3_mission.rule,
                "Reverse Class 3 Race - Gold Medal": reverse_class3_mission.rule,
                "Reverse Class 2 Race - Bronze Medal": reverse_class2_mission.rule,
                "Reverse Class 2 Race - Silver Medal": reverse_class2_mission.rule,
                "Reverse Class 2 Race - Gold Medal": reverse_class2_mission.rule,
                "Reverse Class 1 Race - Bronze Medal": reverse_class1_mission.rule,
                "Reverse Class 1 Race - Silver Medal": reverse_class1_mission.rule,
                "Reverse Class 1 Race - Gold Medal": reverse_class1_mission.rule,
                "City Port Race Side Mission - Bronze Medal": city_port_race_mission.rule,
                "City Port Race Side Mission - Silver Medal": city_port_race_mission.rule,
                "City Port Race Side Mission - Gold Medal": city_port_race_mission.rule,
                "Erol Race - Bronze Medal": erol_race_mission.rule,
                "Erol Race - Silver Medal": erol_race_mission.rule,
                "Erol Race - Gold Medal": erol_race_mission.rule,
            }

            for name, loc_id in get_minigame_medal_locations(True).items():
                rule = medal_rules.get(name, lambda state, player: True)
                mission_tree_region.add_jak_mission(loc_id, name, rule)

        if self.options.orbsanity:
            for name, loc_id in get_orb_locations(True).items():
                rule = orb_names_table.get(name, lambda state, player: True)
                mission_tree_region.add_jak_mission(loc_id, name, rule)

        self.multiworld.regions.append(mission_tree_region)

        # Handle completion condition.
        if self.completion_type == options.CompletionCondition.option_complete_specific_mission:
            mission = all_locations_table[self.completion_value]

            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_location(mission.name, player=self.player))

        elif self.completion_type == options.CompletionCondition.option_complete_number_of_missions:
            def _completion_rule(state, player) -> bool:
                completed_count = 0
                for _, miss in all_locations_table.items():
                    if miss.rule(state, player):
                        completed_count += 1
                return completed_count >= self.completion_value

            self.multiworld.completion_condition[self.player] = lambda state: (
                _completion_rule(state=state, player=self.player))

    def fill_slot_data(self) -> dict[str, Any]:
        from .locs.mission_locations import main_mission_table
        options_dict = self.options.as_dict("jak_2_completion_condition",
                                            "specific_mission_for_completion",
                                            "number_of_missions_for_completion",
                                            "percent_filler_replaced_with_traps",
                                            "trap_effect_duration",
                                            "trap_weights",
                                            "randomize_oracle_cost",
                                            "oracle_cost_level0",
                                            "oracle_cost_level1",
                                            "oracle_cost_level2",
                                            "oracle_cost_level3",
                                            "minigame_medal_checks",
                                            "orbsanity",
                                            "orbs",
                                            )
        # Convert the AP mission_id to GOAL's task_id, since ap-verify-game-completed! compares against task_id.
        mission_id = options_dict["specific_mission_for_completion"]
        options_dict["specific_mission_for_completion"] = main_mission_table[mission_id].task_id
        return options_dict