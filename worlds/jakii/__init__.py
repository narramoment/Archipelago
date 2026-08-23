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
                    TRAP_ID_START, TRAP_ID_END, Jak2ItemData, Jak2Item)
from .locs import (mission_locations)
from .locations import (JakIILocation, all_locations_table)
from .locs.mission_locations import Jak2MissionData
from .regs.region_base import JakIIRegion


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
    location_name_to_id = {data.name: k for k, data in all_locations_table.items()}
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

    def generate_early(self) -> None:
        # Cache completion conditions and values.
        self.completion_type = self.options.jak_2_completion_condition.value  # Sorry about the naming here.
        if self.completion_type == options.CompletionCondition.option_complete_specific_mission:
            self.completion_value = self.options.specific_mission_for_completion.value
        elif self.completion_type == options.CompletionCondition.option_complete_number_of_missions:
            self.completion_value = self.options.number_of_missions_for_completion.value
        else:
            raise OptionError(f"Unknown completion condition selected for Jak II: {self.completion_type}")

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

            data = self.item_data_helper(item_id)
            for (count, classification, num) in data:
                self.multiworld.itempool += [
                    Jak2Item(item_name, classification, item_id, self.player)
                    for _ in range(count)]
                items_made += count

        # Handle Traps (fr!!)
        # Manually filling the item pool with an assortment of traps. Only done if one or more traps have a weight > 0.
        names, weights = self.trap_weights
        if sum(weights):
            total_traps = self.total_trap_items
            trap_list = self.random.choices(names, weights=weights, k=total_traps)
            self.multiworld.itempool += [self.create_item(trap_name) for trap_name in trap_list]
            items_made += total_traps

        # Handle Unfilled Locations!
        all_regions = self.multiworld.get_regions(self.player)
        total_locations = sum(reg.location_count for reg in cast(list[JakIIRegion], all_regions))
        total_filler = total_locations - items_made
        self.multiworld.itempool += [self.create_filler() for _ in range(total_filler)]

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
                                            )
        # Convert the AP mission_id to GOAL's task_id, since ap-verify-game-completed! compares against task_id.
        mission_id = options_dict["specific_mission_for_completion"]
        options_dict["specific_mission_for_completion"] = main_mission_table[mission_id].task_id
        return options_dict
