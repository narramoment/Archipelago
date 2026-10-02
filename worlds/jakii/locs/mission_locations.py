from typing import Callable, Optional
from worlds.jakii.rules import (slums_to_port, slums_to_stadium, slums_to_market, slums_to_landing, slums_to_nest,
                                any_gun)


class Jak2MissionData:
    mission_id: int  # Mission ID is how Archipelago identifies the location.
    task_id: int  # Task ID is how GOAL identifies the location.
    name: str
    rule: Callable

    def __init__(self, mission_id: int, task_id: int, name: str, rule: Optional[Callable] = None):
        self.mission_id = mission_id
        self.task_id = task_id
        self.name = name
        if rule:
            self.rule = rule
        else:
            self.rule = lambda state, player: True


class Jak2SideMissionData:
    mission_id: int  # Mission ID is how Archipelago identifies the location.
    task_id: int  # Task ID is how GOAL identifies the location.
    name: str
    rule: Callable

    def __init__(self, mission_id: int, task_id: int, name: str, rule: Optional[Callable] = None):
        self.mission_id = mission_id
        self.task_id = task_id
        self.name = name
        if rule:
            self.rule = rule
        else:
            self.rule = lambda state, player: True


class Jak2MedalData:
    medal_id: int
    location_id: int
    name: str

    def __init__(self, medal_id: int, location_id: int, name: str):
        self.medal_id = medal_id
        self.location_id = location_id
        self.name = name

class Jak2OrbData:
    orb_id: int
    location_id: int
    name: str
    rule: Callable

    def __init__(self, orb_id: int, location_id: int, name: str, rule: Optional[Callable] = None):
        self.orb_id = orb_id
        self.location_id = location_id
        self.name = name
        if rule:
            self.rule = rule
        else:
            self.rule = lambda state, player: True


# Names for Missions are taken directly from the game
main_mission_table = {
    # Act 1
    1: Jak2MissionData(mission_id=1, task_id=6, name="Fortress: Escape From Prison"),
    2: Jak2MissionData(mission_id=2, task_id=7, name="Haven City: Protect Kor and Kid"),
    3: Jak2MissionData(mission_id=3, task_id=9, name="Dead Town: Retrieve Banner from Dead Town"),
    4: Jak2MissionData(mission_id=4, task_id=10, name="Pumping Station: Find Pumping Station Valve"),
    5: Jak2MissionData(mission_id=5, task_id=11, name="Fortress: Blow up Ammo at Fortress"),
    6: Jak2MissionData(mission_id=6, task_id=12, name="Haven City: Make delivery to Hip Hog Saloon",
                       rule=lambda state, player:
                       state.has("Red Security Pass", player)
                       or state.has_all(("Green Security Pass", "Yellow Security Pass"), player)),
    7: Jak2MissionData(mission_id=7, task_id=13, name="Port: Beat Scatter Gun Course",
                       rule=lambda state, player:
                       slums_to_port(state, player)
                       and state.has("Scatter Gun", player)),
    8: Jak2MissionData(mission_id=8, task_id=14, name="Pumping Station: Protect Sig at Pumping Station",
                       rule=lambda state, player:
                       slums_to_port(state, player)
                       and any_gun(state, player)),
    9: Jak2MissionData(mission_id=9, task_id=15, name="Sewers: Destroy Turrets in Sewers",
                       rule=lambda state, player:
                       slums_to_port(state, player)
                       and any_gun(state, player)),
    10: Jak2MissionData(mission_id=10, task_id=16, name="Strip Mine: Rescue Vin at Strip Mine",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and any_gun(state, player)),
    11: Jak2MissionData(mission_id=11, task_id=17, name="Pumping Station: Find Pumping Station Patrol",
                        rule=lambda state, player: any_gun(state, player)),
    12: Jak2MissionData(mission_id=12, task_id=18, name="Mountain Temple: Find Lens in Mountain Temple",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_any(("Scatter Gun", "Blaster", "Vulcan Fury"), player)),
    13: Jak2MissionData(mission_id=13, task_id=19, name="Mountain Temple: Find Gear in Mountain Temple",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_any(("Scatter Gun", "Blaster", "Vulcan Fury"), player)),
    14: Jak2MissionData(mission_id=14, task_id=20, name="Mountain Temple: Find Shard in Mountain Temple",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_any(("Scatter Gun", "Blaster", "Vulcan Fury"), player)),
    15: Jak2MissionData(mission_id=15, task_id=22, name="Haven City: Beat Time to Race Garage",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and (state.has_all(("Red Security Pass", "Green Security Pass"), player)
                             or state.has("Yellow Security Pass", player))),
    16: Jak2MissionData(mission_id=16, task_id=23, name="Stadium: Win JET-Board Stadium Challenge",
                        rule=lambda state, player:
                        slums_to_stadium(state, player)),
    17: Jak2MissionData(mission_id=17, task_id=24, name="Port: Collect Money for Krew",
                        rule=lambda state, player:
                        slums_to_port(state, player)),
    18: Jak2MissionData(mission_id=18, task_id=25, name="Port: Beat Blaster Gun Course",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("Blaster", player)),
    19: Jak2MissionData(mission_id=19, task_id=26, name="Drill Platform: Destroy Eggs at Drill Platform",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and any_gun(state, player)
                        and state.has("Gunpod", player)),
    20: Jak2MissionData(mission_id=20, task_id=27, name="Haven City, Industrial Sector: Turn on 5 Power Switches",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and ((any_gun(state, player)
                              and state.has("Red Security Pass", player))
                             or (any_gun(state, player)
                                 and state.has_all(("Green Security Pass", "Yellow Security Pass"), player)))),
    21: Jak2MissionData(mission_id=21, task_id=28, name="Palace: Ride Elevator up to Palace",
                        rule=lambda state, player:
                        any_gun(state, player)
                        and slums_to_stadium(state, player)),
    22: Jak2MissionData(mission_id=22, task_id=29, name="Palace: Defeat Baron at Palace",
                        rule=lambda state, player:
                        any_gun(state, player)
                        and slums_to_stadium(state, player)),
    # Act 2 (Palace Baron Fight Complete)
    23: Jak2MissionData(mission_id=23, task_id=30, name="Haven City: Shuttle Underground Fighters"),
    24: Jak2MissionData(mission_id=24, task_id=31, name="Dead Town: Protect Site in Dead Town",
                        rule=lambda state, player:
                        any_gun(state, player)),
    25: Jak2MissionData(mission_id=25, task_id=33, name="Haven Forest: Catch Scouts in Haven Forest",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has("JET-Board", player)),
    26: Jak2MissionData(mission_id=26, task_id=34, name="Haven City: Escort Kid to Power Station",
                        rule=lambda state, player:
                        state.has("Red Security Pass", player)),
    27: Jak2MissionData(mission_id=27, task_id=35, name="Dig Site: Destroy Equipment at Dig",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("JET-Board", player)),
    28: Jak2MissionData(mission_id=28, task_id=36, name="Strip Mine: Blow up Strip Mine Eco Wells",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("JET-Board", player)),
    29: Jak2MissionData(mission_id=29, task_id=37, name="Drill Platform: Destroy Ship at Drill Platform",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("Gunpod", player)),
    30: Jak2MissionData(mission_id=30, task_id=38, name="Port: Destroy Cargo in Port",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("JET-Board", player)),
    31: Jak2MissionData(mission_id=31, task_id=39, name="Haven City, West Marketplace: Rescue Lurkers for Brutter #1",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and any_gun(state, player)
                        and state.has("Yellow Security Pass", player)),
    32: Jak2MissionData(mission_id=32, task_id=40, name="Sewers: Drain Sewers to find Statue",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("JET-Board", player)),
    33: Jak2MissionData(mission_id=33, task_id=41, name="Haven Forest: Hunt Haven Forest Metal Heads",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and any_gun(state, player)
                        and state.has("Yellow Security Pass", player)),
    34: Jak2MissionData(mission_id=34, task_id=42, name="Haven City, West Marketplace: Intercept Tanker",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and (any_gun(state, player)
                             or state.has("Dark Jak", player))),
    35: Jak2MissionData(mission_id=35, task_id=43, name="Stadium: Win Class 3 Race at Stadium",
                        rule=lambda state, player:
                        slums_to_stadium(state, player)),
    36: Jak2MissionData(mission_id=36, task_id=44, name="Water Slums: Get Seal Piece at Water Slums",
                        rule=lambda state, player:
                        any_gun(state, player)
                        or state.has("JET-Board", player)),
    37: Jak2MissionData(mission_id=37, task_id=45, name="Dig Site: Get Seal Piece at Dig",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and any_gun(state, player)
                        and state.has("JET-Board", player)),
    38: Jak2MissionData(mission_id=38, task_id=46, name="Haven City: Destroy 5 HellCat Cruisers",
                        rule=lambda state, player:
                        state.has("Red Security Pass", player)
                        and any_gun(state, player)),
    39: Jak2MissionData(mission_id=39, task_id=47, name="Haven City, Bazaar: Beat Onin Game",
                        rule=lambda state, player:
                        slums_to_market(state, player)),
    40: Jak2MissionData(mission_id=40, task_id=48, name="No Man's Canyon: Use items in No Man's Canyon",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has("JET-Board", player)
                        and state.has_all(("Seal Piece #1", "Seal Piece #2", "Seal Piece #3"), player)),
    41: Jak2MissionData(mission_id=41, task_id=49, name="Mar's Tomb: Pass the first Test of Manhood",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_all(("Lens", "Gear", "Shard"), player)),
    42: Jak2MissionData(mission_id=42, task_id=50, name="Mar's Tomb: Pass the second Test of Manhood",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_all(("Lens", "Gear", "Shard"), player)),
    43: Jak2MissionData(mission_id=43, task_id=51, name="Mar's Tomb: Defeat Baron in Mar's Tomb",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and any_gun(state, player)
                        and state.has_all(("Lens", "Gear", "Shard"), player)),
    # Act 3 (Tomb Baron Fight Complete)
    44: Jak2MissionData(mission_id=44, task_id=52, name="Fortress: Rescue Friends in Fortress",
                        rule=lambda state, player:
                        any_gun(state, player)
                        and state.has("JET-Board", player)),
    45: Jak2MissionData(mission_id=45, task_id=53, name="Sewers: Escort men through Sewers",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and any_gun(state, player)),
    46: Jak2MissionData(mission_id=46, task_id=55, name="Stadium: Win Class 2 Race at Stadium",
                        rule=lambda state, player:
                        slums_to_stadium(state, player)),
    47: Jak2MissionData(mission_id=47, task_id=56, name="Haven City: Protect Hideout from Bombots",
                        rule=lambda state, player:
                        state.has_all(("Red Security Pass", "Vulcan Fury"), player)),
    48: Jak2MissionData(mission_id=48, task_id=57, name="Haven City: Beat Erol in Race Challenge",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("Yellow Security Pass", player)),
    49: Jak2MissionData(mission_id=49, task_id=58, name="Strip Mine: Destroy Eggs in Strip Mine",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has("JET-Board", player)),
    50: Jak2MissionData(mission_id=50, task_id=59, name="Dead Town: Get Life Seed in Dead Town",
                        rule=lambda state, player:
                        any_gun(state, player)
                        and state.has("Titan Suit", player)),
    51: Jak2MissionData(mission_id=51, task_id=60, name="Haven Forest: Protect Samos in Haven Forest",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and any_gun(state, player)
                        and state.has("Life Seed", player)),
    52: Jak2MissionData(mission_id=52, task_id=61, name="Drill Platform: Destroy Drill Platform Tower",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and (state.has("Titan Suit", player)
                             and state.has_any(("Blaster", "Vulcan Fury"), player))),
    53: Jak2MissionData(mission_id=53, task_id=62, name="Haven City, West Marketplace: Rescue Lurkers for Brutter #2",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and (state.has("Yellow Security Pass", player))
                        and any_gun(state, player)),
    54: Jak2MissionData(mission_id=54, task_id=63, name="Stadium: Win Class 1 Race at Stadium",
                        rule=lambda state, player:
                        slums_to_stadium(state, player)),
    55: Jak2MissionData(mission_id=55, task_id=64, name="Palace: Explore Palace",
                        rule=lambda state, player:
                        slums_to_market(state, player)
                        and state.has_all(("JET-Board", "Purple Security Pass"), player)
                        and any_gun(state, player)),
    56: Jak2MissionData(mission_id=56, task_id=65, name="Weapons Lab: Get Heart of Mar in Weapons Lab",
                        rule=lambda state, player:
                        slums_to_landing(state, player)
                        and state.has("Black Security Pass", player)
                        and any_gun(state, player)),
    57: Jak2MissionData(mission_id=57, task_id=66, name="Weapons Lab: Beat Krew in Weapons Lab",
                        rule=lambda state, player:
                        slums_to_landing(state, player)
                        and state.has("Black Security Pass", player)
                        and any_gun(state, player)),
    58: Jak2MissionData(mission_id=58, task_id=67, name="Hip-Hog Saloon: Beat the Metal Head Mash Game",
                        rule=lambda state, player:
                        slums_to_port(state, player)),
    59: Jak2MissionData(mission_id=59, task_id=68, name="Under Port: Find Sig in Under Port",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has_all(("Ruby Key", "Titan Suit"), player)),
    60: Jak2MissionData(mission_id=60, task_id=69, name="Under Port: Escort Sig in Under Port",
                        rule=lambda state, player:
                        slums_to_port(state, player)
                        and state.has_all(("Ruby Key", "Titan Suit"), player)
                        and any_gun(state, player)),
    61: Jak2MissionData(mission_id=61, task_id=70, name="Stadium: Defend Stadium",
                        rule=lambda state, player:
                        slums_to_stadium(state, player)
                        and state.has_all(("Heart of Mar", "Time Map", "Rift Rider"), player)
                        and any_gun(state, player)),
    62: Jak2MissionData(mission_id=62, task_id=71, name="Construction Site: Check the Construction Site",
                        rule=lambda state, player:
                        slums_to_port(state, player)),
    63: Jak2MissionData(mission_id=63, task_id=72, name="Metal Head Nest: Break Barrier at Nest",
                        rule=lambda state, player:
                        slums_to_nest(state, player)
                        and state.has("Precursor Stone", player)
                        and any_gun(state, player)),
    64: Jak2MissionData(mission_id=64, task_id=73, name="Metal Head Nest: Attack the Metal Head Nest",
                        rule=lambda state, player:
                        slums_to_nest(state, player)
                        and state.has("Precursor Stone", player)
                        and any_gun(state, player)),
    65: Jak2MissionData(mission_id=65, task_id=74, name="Metal Head Nest: Destroy Metal Kor at Nest",
                        rule=lambda state, player:
                        slums_to_nest(state, player)
                        and state.has_all(("Heart of Mar", "Time Map", "Rift Rider", "Precursor Stone", "Dark Jak"),
                                          player)
                        and any_gun(state, player))
}


main_tasks_to_missions = {miss.task_id: miss for _, miss in main_mission_table.items()}


# Names of Side Missions are taken from the Fandom Jak II Wiki
# ID numbers are precalculated and offset by 100 to distinguish them from main missions.
side_mission_table = {
    # Orb Searches
    101: Jak2SideMissionData(mission_id=101, task_id=78, name="Orb Search 1 (Computer #2)"),
    102: Jak2SideMissionData(mission_id=102, task_id=79, name="Orb Search 2 (Computer #3)",
                             rule=lambda state, player:
                             slums_to_port(state, player)),
    103: Jak2SideMissionData(mission_id=103, task_id=80, name="Orb Search 3 (Computer #4)",
                             rule=lambda state, player:
                             slums_to_port(state, player)),
    104: Jak2SideMissionData(mission_id=104, task_id=81, name="Orb Search 4 (Computer #5)"),
    105: Jak2SideMissionData(mission_id=105, task_id=85, name="Orb Search 5 (Computer #9)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    106: Jak2SideMissionData(mission_id=106, task_id=86, name="Orb Search 6 (Computer #10)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    107: Jak2SideMissionData(mission_id=107, task_id=88, name="Orb Search 7 (Computer #11)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    108: Jak2SideMissionData(mission_id=108, task_id=89, name="Orb Search 8 (Computer #12)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    109: Jak2SideMissionData(mission_id=109, task_id=90, name="Orb Search 9 (Computer #6)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    110: Jak2SideMissionData(mission_id=110, task_id=92, name="Orb Search 10 (Computer #14)",
                             rule=lambda state, player:
                             slums_to_port(state, player)),
    111: Jak2SideMissionData(mission_id=111, task_id=93, name="Orb Search 11 (Computer #15)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    112: Jak2SideMissionData(mission_id=112, task_id=95, name="Orb Search 12 (Computer #7)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    113: Jak2SideMissionData(mission_id=113, task_id=97, name="Orb Search 13 (Computer #16)",
                             rule=lambda state, player:
                             state.has("Green Security Pass", player)),
    114: Jak2SideMissionData(mission_id=114, task_id=98, name="Orb Search 14 (Computer #17)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    115: Jak2SideMissionData(mission_id=115, task_id=99, name="Orb Search 15 (Computer #18)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    # Ring Races
    116: Jak2SideMissionData(mission_id=116, task_id=77, name="Ring Race 1 (Computer #1)"),
    117: Jak2SideMissionData(mission_id=117, task_id=84, name="Ring Race 2 (Computer #8)",
                             rule=lambda state, player:
                             slums_to_port(state, player)
                             and state.has("Yellow Security Pass", player)),
    118: Jak2SideMissionData(mission_id=118, task_id=94, name="Ring Race 3 (Computer #1)",
                             rule=lambda state, player:
                             state.has("Red Security Pass", player)),
    # Collect-em-alls
    119: Jak2SideMissionData(mission_id=119, task_id=82, name="Collection 1 (Computer #6)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    120: Jak2SideMissionData(mission_id=120, task_id=91, name="Collection 2 (Computer #13)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    121: Jak2SideMissionData(mission_id=121, task_id=100, name="Collection 3 (Computer #12)",
                             rule=lambda state, player:
                             slums_to_market(state, player)),
    # Missions Turned Side Missions
    122: Jak2SideMissionData(mission_id=122, task_id=83, name="Make Delivery to Hideout Side Mission (Computer #7)",
                             rule=lambda state, player:
                             state.has_all(("Red Security Pass", "Yellow Security Pass"), player)),
    123: Jak2SideMissionData(mission_id=123, task_id=87, name="Shuttle Underground Fighters Side Mission (Computer #7)",
                             rule=lambda state, player:
                             state.has_all(("Red Security Pass", "Yellow Security Pass"), player)),
    124: Jak2SideMissionData(mission_id=124, task_id=96, name="Destroy Blast Bots Side Mission (Computer #7)",
                             rule=lambda state, player:
                             slums_to_market(state, player)
                             and state.has("Yellow Security Pass", player)),
    # Extra Race Missions
    125: Jak2SideMissionData(mission_id=125, task_id=101,
                             name="Beat Erol in Race Challenge (Side Mission, Near Hip Hog)",
                             rule=lambda state, player:
                             slums_to_port(state, player)
                             and state.has("Yellow Security Pass", player)),
    126: Jak2SideMissionData(mission_id=126, task_id=102,
                             name="Port Race Side Mission (Near Port/Industrial Connection)",
                             rule=lambda state, player:
                             slums_to_port(state, player)),
    # Stadium Challenges
    127: Jak2SideMissionData(mission_id=127, task_id=103, name="JET-Board Stadium Challenge (Side Mission)",
                             rule=lambda state, player:
                             state.has("JET-Board", player)
                             and slums_to_stadium(state, player)),
    128: Jak2SideMissionData(mission_id=128, task_id=104, name="Class 3 Race (Side Mission, Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    129: Jak2SideMissionData(mission_id=129, task_id=105, name="Class 2 Race (Side Mission, Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    130: Jak2SideMissionData(mission_id=130, task_id=106, name="Class 1 Race (Side Mission, Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    131: Jak2SideMissionData(mission_id=131, task_id=107, name="Class 3 Reverse Race (Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    132: Jak2SideMissionData(mission_id=132, task_id=108, name="Class 2 Reverse Race (Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player)),
    133: Jak2SideMissionData(mission_id=133, task_id=109, name="Class 1 Reverse Race (Stadium)",
                             rule=lambda state, player:
                             slums_to_stadium(state, player))
}
side_tasks_to_missions = {miss.task_id: miss for _, miss in side_mission_table.items()}


# Item IDs match the game-feature enum values in GOAL (ap-struct.gc / *ap-tracked-items*).
# Location IDs for individually-tracked items are offset by 10000 to avoid colliding with mission IDs.
# task_id is unused for these entries (not tied to any game-task), left as 0.
ITEM_CHECK_LOCATION_OFFSET = 10000

item_check_table = {
    ITEM_CHECK_LOCATION_OFFSET + 13: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 13,
                                                     task_id=0,
                                                     name="Dark Jak",
                                                     rule=lambda state, player:
                                                     main_mission_table[2].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 18: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 18,
                                                     task_id=0,
                                                     name="Red Security Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[5].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 7:  Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 7,
                                                     task_id=0,
                                                     name="Scatter Gun",
                                                     rule=lambda state, player:
                                                     main_mission_table[6].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 6:  Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 6,
                                                     task_id=0,
                                                     name="Blaster",
                                                     rule=lambda state, player:
                                                     main_mission_table[9].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 30: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 30,
                                                     task_id=0,
                                                     name="Mountain Lens",
                                                     rule=lambda state, player:
                                                     main_mission_table[12].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 31: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 31,
                                                     task_id=0,
                                                     name="Mountain Gear",
                                                     rule=lambda state, player:
                                                     main_mission_table[13].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 32: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 32,
                                                     task_id=0,
                                                     name="Mountain Shard",
                                                     rule=lambda state, player:
                                                     main_mission_table[14].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 39: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 39,
                                                     task_id=0,
                                                     name="Gun Turret",
                                                     rule=lambda state, player:
                                                     main_mission_table[19].rule(state, player)
                                                     or main_mission_table[29].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 20: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 20,
                                                     task_id=0,
                                                     name="Yellow Security Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[11].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 19: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 19,
                                                     task_id=0,
                                                     name="Green Security Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[15].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 14: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 14,
                                                     task_id=0,
                                                     name="Gun Speed Upgrade",
                                                     rule=lambda state, player:
                                                     main_mission_table[17].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 29: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 29,
                                                     task_id=0,
                                                     name="Air Train Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[26].rule(state, player)
                                                     or main_mission_table[27].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 8:  Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 8,
                                                     task_id=0,
                                                     name="Vulcan Fury",
                                                     rule=lambda state, player:
                                                     main_mission_table[24].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 10: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 10,
                                                     task_id=0,
                                                     name="JET-Board",
                                                     rule=lambda state, player:
                                                     main_mission_table[25].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 40: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 40,
                                                     task_id=0,
                                                     name="Seal Piece 1",
                                                     rule=lambda state, player:
                                                     main_mission_table[36].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 41: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 41,
                                                     task_id=0,
                                                     name="Seal Piece 2",
                                                     rule=lambda state, player:
                                                     main_mission_table[37].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 42: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 42,
                                                     task_id=0,
                                                     name="Seal Piece 3",
                                                     rule=lambda state, player:
                                                     main_mission_table[39].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 33: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 33,
                                                     task_id=0,
                                                     name="Ruby Key",
                                                     rule=lambda state, player:
                                                     main_mission_table[32].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 15: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 15,
                                                     task_id=0,
                                                     name="Gun Ammo Upgrade",
                                                     rule=lambda state, player:
                                                     main_mission_table[31].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 9:  Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 9,
                                                     task_id=0,
                                                     name="Peacemaker",
                                                     rule=lambda state, player:
                                                     main_mission_table[45].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 38: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 38,
                                                     task_id=0,
                                                     name="Titan Suit",
                                                     rule=lambda state, player:
                                                     main_mission_table[50].rule(state, player)
                                                     or main_mission_table[52].rule(state, player)
                                                     or main_mission_table[59].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 37: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 37,
                                                     task_id=0,
                                                     name="Life Seed",
                                                     rule=lambda state, player:
                                                     main_mission_table[50].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 27: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 27,
                                                     task_id=0,
                                                     name="Purple Security Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[54].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 28: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 28,
                                                     task_id=0, name="Black Security Pass",
                                                     rule=lambda state, player:
                                                     main_mission_table[55].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 16: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 16,
                                                     task_id=0, name="Gun Damage Upgrade",
                                                     rule=lambda state, player:
                                                     main_mission_table[43].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 34: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 34,
                                                     task_id=0,
                                                     name="Heart of Mar",
                                                     rule=lambda state, player:
                                                     main_mission_table[43].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 35: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 35,
                                                     task_id=0,
                                                     name="Time Map",
                                                     rule=lambda state, player:
                                                     main_mission_table[58].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 43: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 43,
                                                     task_id=0,
                                                     name="Rift Rider",
                                                     rule=lambda state, player:
                                                     main_mission_table[61].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 36: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 36,
                                                     task_id=0,
                                                     name="Precursor Stone",
                                                     rule=lambda state, player:
                                                     main_mission_table[62].rule(state, player)),
    ITEM_CHECK_LOCATION_OFFSET + 22: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 22,
                                                     task_id=0, name="Dark Bomb",
                                                     rule= lambda state, player:
                                                     state.has("Dark Jak", player)),
    ITEM_CHECK_LOCATION_OFFSET + 23: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 23,
                                                     task_id=0, name="Dark Blast",
                                                     rule = lambda state, player:
                                                     state.has("Dark Jak", player)),
    ITEM_CHECK_LOCATION_OFFSET + 24: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 24,
                                                     task_id=0, name="Dark Invincibility",
                                                     rule = lambda state, player:
                                                     state.has ("Dark Jak", player)),
    ITEM_CHECK_LOCATION_OFFSET + 25: Jak2MissionData(mission_id=ITEM_CHECK_LOCATION_OFFSET + 25,
                                                     task_id=0,
                                                     name="Dark Giant",
                                                     rule = lambda state, player:
                                                     state.has("Dark Jak", player)),
}


def get_item_id_by_feature_id(game_feature_id: int) -> int | None:
    """Given a raw game-feature ID read from memory, return the AP location ID for that item check, or None."""
    loc_id = ITEM_CHECK_LOCATION_OFFSET + game_feature_id
    if loc_id in item_check_table:
        return loc_id
    return None


# Minigame bronze/silver/gold medal locations. Only included when the
# Minigame Medal Checks option is enabled.
# Location IDs are offset by 20000 to avoid colliding with missions (1-133) and item checks (10000+).
MEDAL_LOCATION_OFFSET = 20000

minigame_medal_table = {
    1: Jak2MedalData(medal_id=1, location_id=MEDAL_LOCATION_OFFSET + 1, name="Scatter Gun Course - Bronze Medal"),
    2: Jak2MedalData(medal_id=2, location_id=MEDAL_LOCATION_OFFSET + 2, name="Scatter Gun Course - Silver Medal"),
    3: Jak2MedalData(medal_id=3, location_id=MEDAL_LOCATION_OFFSET + 3, name="Scatter Gun Course - Gold Medal"),
    4: Jak2MedalData(medal_id=4, location_id=MEDAL_LOCATION_OFFSET + 4, name="Blaster Gun Course - Bronze Medal"),
    5: Jak2MedalData(medal_id=5, location_id=MEDAL_LOCATION_OFFSET + 5, name="Blaster Gun Course - Silver Medal"),
    6: Jak2MedalData(medal_id=6, location_id=MEDAL_LOCATION_OFFSET + 6, name="Blaster Gun Course - Gold Medal"),
    7: Jak2MedalData(medal_id=7, location_id=MEDAL_LOCATION_OFFSET + 7, name="Vulcan Fury Gun Course - Bronze Medal"),
    8: Jak2MedalData(medal_id=8, location_id=MEDAL_LOCATION_OFFSET + 8, name="Vulcan Fury Gun Course - Silver Medal"),
    9: Jak2MedalData(medal_id=9, location_id=MEDAL_LOCATION_OFFSET + 9, name="Vulcan Fury Gun Course - Gold Medal"),
    10: Jak2MedalData(medal_id=10, location_id=MEDAL_LOCATION_OFFSET + 10, name="Peacemaker Gun Course - Bronze Medal"),
    11: Jak2MedalData(medal_id=11, location_id=MEDAL_LOCATION_OFFSET + 11, name="Peacemaker Gun Course - Silver Medal"),
    12: Jak2MedalData(medal_id=12, location_id=MEDAL_LOCATION_OFFSET + 12, name="Peacemaker Gun Course - Gold Medal"),
    13: Jak2MedalData(medal_id=13, location_id=MEDAL_LOCATION_OFFSET + 13, name="Onin's Game - Medal"),
    14: Jak2MedalData(medal_id=14, location_id=MEDAL_LOCATION_OFFSET + 14, name="JET-Board Challenge - Bronze Medal"),
    15: Jak2MedalData(medal_id=15, location_id=MEDAL_LOCATION_OFFSET + 15, name="JET-Board Challenge - Silver Medal"),
    16: Jak2MedalData(medal_id=16, location_id=MEDAL_LOCATION_OFFSET + 16, name="JET-Board Challenge - Gold Medal"),
    17: Jak2MedalData(medal_id=17, location_id=MEDAL_LOCATION_OFFSET + 17, name="Class 3 Race - Bronze Medal"),
    18: Jak2MedalData(medal_id=18, location_id=MEDAL_LOCATION_OFFSET + 18, name="Class 3 Race - Silver Medal"),
    19: Jak2MedalData(medal_id=19, location_id=MEDAL_LOCATION_OFFSET + 19, name="Class 3 Race - Gold Medal"),
    20: Jak2MedalData(medal_id=20, location_id=MEDAL_LOCATION_OFFSET + 20, name="Class 2 Race - Bronze Medal"),
    21: Jak2MedalData(medal_id=21, location_id=MEDAL_LOCATION_OFFSET + 21, name="Class 2 Race - Silver Medal"),
    22: Jak2MedalData(medal_id=22, location_id=MEDAL_LOCATION_OFFSET + 22, name="Class 2 Race - Gold Medal"),
    23: Jak2MedalData(medal_id=23, location_id=MEDAL_LOCATION_OFFSET + 23, name="Class 1 Race - Bronze Medal"),
    24: Jak2MedalData(medal_id=24, location_id=MEDAL_LOCATION_OFFSET + 24, name="Class 1 Race - Silver Medal"),
    25: Jak2MedalData(medal_id=25, location_id=MEDAL_LOCATION_OFFSET + 25, name="Class 1 Race - Gold Medal"),
    26: Jak2MedalData(medal_id=26, location_id=MEDAL_LOCATION_OFFSET + 26, name="Reverse Class 3 Race - Bronze Medal"),
    27: Jak2MedalData(medal_id=27, location_id=MEDAL_LOCATION_OFFSET + 27, name="Reverse Class 3 Race - Silver Medal"),
    28: Jak2MedalData(medal_id=28, location_id=MEDAL_LOCATION_OFFSET + 28, name="Reverse Class 3 Race - Gold Medal"),
    29: Jak2MedalData(medal_id=29, location_id=MEDAL_LOCATION_OFFSET + 29, name="Reverse Class 2 Race - Bronze Medal"),
    30: Jak2MedalData(medal_id=30, location_id=MEDAL_LOCATION_OFFSET + 30, name="Reverse Class 2 Race - Silver Medal"),
    31: Jak2MedalData(medal_id=31, location_id=MEDAL_LOCATION_OFFSET + 31, name="Reverse Class 2 Race - Gold Medal"),
    32: Jak2MedalData(medal_id=32, location_id=MEDAL_LOCATION_OFFSET + 32, name="Reverse Class 1 Race - Bronze Medal"),
    33: Jak2MedalData(medal_id=33, location_id=MEDAL_LOCATION_OFFSET + 33, name="Reverse Class 1 Race - Silver Medal"),
    34: Jak2MedalData(medal_id=34, location_id=MEDAL_LOCATION_OFFSET + 34, name="Reverse Class 1 Race - Gold Medal"),
    35: Jak2MedalData(medal_id=35, location_id=MEDAL_LOCATION_OFFSET + 35, name="City Port Race Side Mission - Bronze Medal"),
    36: Jak2MedalData(medal_id=36, location_id=MEDAL_LOCATION_OFFSET + 36, name="City Port Race Side Mission - Silver Medal"),
    37: Jak2MedalData(medal_id=37, location_id=MEDAL_LOCATION_OFFSET + 37, name="City Port Race Side Mission - Gold Medal"),
    38: Jak2MedalData(medal_id=38, location_id=MEDAL_LOCATION_OFFSET + 38, name="Erol Race - Bronze Medal"),
    39: Jak2MedalData(medal_id=39, location_id=MEDAL_LOCATION_OFFSET + 39, name="Erol Race - Silver Medal"),
    40: Jak2MedalData(medal_id=40, location_id=MEDAL_LOCATION_OFFSET + 40, name="Erol Race - Gold Medal"),
}

medal_ids_to_medals = {medal_id: medal for medal_id, medal in minigame_medal_table.items()}


def get_minigame_medal_locations(medal_checks_enabled: bool) -> dict[str, int]:
    if not medal_checks_enabled:
        return {}
    return {medal.name: medal.location_id for medal in minigame_medal_table.values()}

# Orb locations, only included if orbsanity is enabled. Location IDs are offset by 30000 to avoid colliding with
# missions, items, and medals.
ORB_LOCATION_OFFSET = 30000

orb_names_table = {
    # Real freestanding orbs (1-94)
    1: Jak2OrbData(orb_id=1, location_id=ORB_LOCATION_OFFSET + 1, name="Fortress - Orb 1"),
    2: Jak2OrbData(orb_id=2, location_id=ORB_LOCATION_OFFSET + 2, name="Fortress - Orb 2"),
    3: Jak2OrbData(orb_id=3, location_id=ORB_LOCATION_OFFSET + 3, name="Fortress - Orb 3"),
    4: Jak2OrbData(orb_id=4, location_id=ORB_LOCATION_OFFSET + 4, name="Fortress - Orb 4"),
    5: Jak2OrbData(orb_id=5, location_id=ORB_LOCATION_OFFSET + 5, name="Fortress - Orb 5"),
    6: Jak2OrbData(orb_id=6, location_id=ORB_LOCATION_OFFSET + 6, name="Fortress - Orb 6"),
    7: Jak2OrbData(orb_id=7, location_id=ORB_LOCATION_OFFSET + 7, name="Fortress - Orb 7"),
    8: Jak2OrbData(orb_id=8, location_id=ORB_LOCATION_OFFSET + 8, name="Fortress - Orb 8"),
    9: Jak2OrbData(orb_id=9, location_id=ORB_LOCATION_OFFSET + 9, name="Palace Elevator - Orb 1",
                   rule=lambda state, player: main_mission_table[21].rule(state, player)),
    10: Jak2OrbData(orb_id=10, location_id=ORB_LOCATION_OFFSET + 10, name="Palace Cable - Orb 1",
                    rule=lambda state, player: main_mission_table[22].rule(state, player)),
    11: Jak2OrbData(orb_id=11, location_id=ORB_LOCATION_OFFSET + 11, name="Palace Cable - Orb 2",
                    rule=lambda state, player:main_mission_table[22].rule(state, player)),
    12: Jak2OrbData(orb_id=12, location_id=ORB_LOCATION_OFFSET + 12, name="Palace Roof - Orb 1",
                    rule=lambda state, player: main_mission_table[22].rule(state, player)),
    13: Jak2OrbData(orb_id=13, location_id=ORB_LOCATION_OFFSET + 13, name="Weapons Factory - Orb 1",
                    rule=lambda state, player: main_mission_table[56].rule(state, player)),
    14: Jak2OrbData(orb_id=14, location_id=ORB_LOCATION_OFFSET + 14, name="Weapons Factory - Orb 2",
                    rule=lambda state, player: main_mission_table[56].rule(state, player)),
    15: Jak2OrbData(orb_id=15, location_id=ORB_LOCATION_OFFSET + 15, name="Weapons Factory - Orb 3",
                    rule=lambda state, player: main_mission_table[56].rule(state, player)),
    16: Jak2OrbData(orb_id=16, location_id=ORB_LOCATION_OFFSET + 16, name="Weapons Factory - Orb 4",
                    rule=lambda state, player: main_mission_table[56].rule(state, player)),
    17: Jak2OrbData(orb_id=17, location_id=ORB_LOCATION_OFFSET + 17, name="Weapons Factory - Orb 5",
                    rule=lambda state, player: main_mission_table[56].rule(state, player)),
    18: Jak2OrbData(orb_id=18, location_id=ORB_LOCATION_OFFSET + 18, name="Dead Town - Orb 1",
                    rule=lambda state, player: state.has("JET-Board", player)),
    19: Jak2OrbData(orb_id=19, location_id=ORB_LOCATION_OFFSET + 19, name="Dead Town - Orb 2",
                    rule=lambda state, player: state.has("JET-Board", player)),
    20: Jak2OrbData(orb_id=20, location_id=ORB_LOCATION_OFFSET + 20, name="Dead Town - Orb 3",
                    rule=lambda state, player: state.has("JET-Board", player)),
    21: Jak2OrbData(orb_id=21, location_id=ORB_LOCATION_OFFSET + 21, name="Dead Town - Orb 4",
                    rule=lambda state, player: state.has("JET-Board", player)),
    22: Jak2OrbData(orb_id=22, location_id=ORB_LOCATION_OFFSET + 22, name="Dead Town - Orb 5",
                    rule=lambda state, player: state.has("JET-Board", player)),
    23: Jak2OrbData(orb_id=23, location_id=ORB_LOCATION_OFFSET + 23, name="Dead Town - Orb 6",
                    rule=lambda state, player: state.has("JET-Board", player)),
    24: Jak2OrbData(orb_id=24, location_id=ORB_LOCATION_OFFSET + 24, name="Dead Town - Orb 7",
                    rule=lambda state, player: main_mission_table[50].rule(state, player)),
    25: Jak2OrbData(orb_id=25, location_id=ORB_LOCATION_OFFSET + 25, name="Dead Town - Orb 8",
                    rule=lambda state, player: main_mission_table[50].rule(state, player)),
    26: Jak2OrbData(orb_id=26, location_id=ORB_LOCATION_OFFSET + 26, name="Pumping Station - Orb 1"),
    27: Jak2OrbData(orb_id=27, location_id=ORB_LOCATION_OFFSET + 27, name="Pumping Station - Orb 2"),
    28: Jak2OrbData(orb_id=28, location_id=ORB_LOCATION_OFFSET + 28, name="Pumping Station - Orb 3",
                    rule=lambda state, player: main_mission_table[8].rule(state, player)),
    29: Jak2OrbData(orb_id=29, location_id=ORB_LOCATION_OFFSET + 29, name="Pumping Station - Orb 4"),
    30: Jak2OrbData(orb_id=30, location_id=ORB_LOCATION_OFFSET + 30, name="Pumping Station - Orb 5"),
    31: Jak2OrbData(orb_id=31, location_id=ORB_LOCATION_OFFSET + 31, name="Pumping Station - Orb 6"),
    32: Jak2OrbData(orb_id=32, location_id=ORB_LOCATION_OFFSET + 32, name="Pumping Station - Orb 7"),
    33: Jak2OrbData(orb_id=33, location_id=ORB_LOCATION_OFFSET + 33, name="Sewers - Orb 1",
                    rule=lambda state, player: main_mission_table[32].rule(state, player)),
    # 34: "Strip Mine - Orb 1",
    # 35: "Strip Mine - Orb 2",
    # 36: "Strip Mine - Orb 3",
    # 37: "Strip Mine - Orb 4",
    # 38: "Strip Mine - Orb 5",
    # 39: "Strip Mine - Orb 6",
    # 40: "Strip Mine - Orb 7",
    # 41: "Mountain Temple - Orb 1",
    # 42: "Mountain Temple - Orb 2",
    # 43: "Mountain Temple - Orb 3",
    # 44: "Mountain Temple - Orb 4",
    # 45: "Mountain Temple - Orb 5",
    # 46: "Mountain Temple - Orb 6",
    # 47: "Mountain Temple - Orb 7",
    # 48: "Mountain Temple - Orb 8",
    # 49: "Mountain Temple - Orb 9",
    # 50: "Mountain Temple - Orb 10",
    # 51: "Mountain Temple - Orb 11",
    # 52: "Mountain Temple - Orb 12",
    # 53: "Mountain Temple - Orb 13",
    # 54: "Mountain Temple - Orb 14",
    # 55: "Mountain Temple - Orb 15",
    # 56: "Mountain Temple - Orb 16",
    # 57: "Mountain Temple - Orb 17",
    # 58: "Haven Forest - Orb 1",
    # 59: "Haven Forest - Orb 2",
    # 60: "Haven Forest - Orb 3",
    # 61: "Haven Forest - Orb 4",
    # 62: "Haven Forest - Orb 5",
    # 63: "Haven Forest - Orb 6",
    # 64: "Haven Forest - Orb 7",
    # 65: "Haven Forest - Orb 8",
    # 66: "Haven Forest - Orb 9",
    # 67: "Drill Platform - Orb 1",
    # 68: "Drill Platform - Orb 2",
    # 69: "Drill Platform - Orb 3",
    # 70: "Drill Platform - Orb 4",
    # 71: "Drill Platform - Orb 5",
    # 72: "Mar's Tomb - Orb 1",
    # 73: "Mar's Tomb - Orb 2",
    # 74: "Mar's Tomb - Orb 3",
    # 75: "Mar's Tomb - Orb 4",
    # 76: "Mar's Tomb - Orb 5",
    # 77: "Dig Site - Orb 1",
    # 78: "Dig Site - Orb 2",
    # 79: "Dig Site - Orb 3",
    # 80: "Dig Site - Orb 4",
    # 81: "Dig Site - Orb 5",
    # 82: "Dig Site - Orb 6",
    # 83: "Dig Site - Orb 7",
    # 84: "Dig Site - Orb 8",
    # 85: "Construction Site - Orb 1",
    # 86: "Construction Site - Orb 2",
    # 87: "Under Port - Orb 1",
    # 88: "Metal Head Nest - Orb 1",
    # 89: "Metal Head Nest - Orb 2",
    # 90: "Metal Head Nest - Orb 3",
    # 91: "Metal Head Nest - Orb 4",
    # 92: "Metal Head Nest - Orb 5",
    # 93: "Metal Head Nest - Orb 6",
    # 94: "Metal Head Nest - Orb 7",
    # # Synthetic orb-equivalents from minigames/tasks (95-241)
    # 95: "Onin's Game - Orb 1",
    # 96: "Onin's Game - Orb 2",
    # 97: "Onin's Game - Orb 3",
    # 98: "Scatter Gun Course - Orb 1",
    # 99: "Scatter Gun Course - Orb 2",
    # 100: "Scatter Gun Course - Orb 3",
    # 101: "Scatter Gun Course - Orb 4",
    # 102: "Scatter Gun Course - Orb 5",
    # 103: "Scatter Gun Course - Orb 6",
    # 104: "Scatter Gun Course - Orb 7",
    # 105: "Scatter Gun Course - Orb 8",
    # 106: "Scatter Gun Course - Orb 9",
    # 107: "Blaster Gun Course - Orb 1",
    # 108: "Blaster Gun Course - Orb 2",
    # 109: "Blaster Gun Course - Orb 3",
    # 110: "Blaster Gun Course - Orb 4",
    # 111: "Blaster Gun Course - Orb 5",
    # 112: "Blaster Gun Course - Orb 6",
    # 113: "Blaster Gun Course - Orb 7",
    # 114: "Blaster Gun Course - Orb 8",
    # 115: "Blaster Gun Course - Orb 9",
    # 116: "Vulcan Fury Gun Course - Orb 1",
    # 117: "Vulcan Fury Gun Course - Orb 2",
    # 118: "Vulcan Fury Gun Course - Orb 3",
    # 119: "Vulcan Fury Gun Course - Orb 4",
    # 120: "Vulcan Fury Gun Course - Orb 5",
    # 121: "Vulcan Fury Gun Course - Orb 6",
    # 122: "Vulcan Fury Gun Course - Orb 7",
    # 123: "Vulcan Fury Gun Course - Orb 8",
    # 124: "Vulcan Fury Gun Course - Orb 9",
    # 125: "Peacemaker Gun Course - Orb 1",
    # 126: "Peacemaker Gun Course - Orb 2",
    # 127: "Peacemaker Gun Course - Orb 3",
    # 128: "Peacemaker Gun Course - Orb 4",
    # 129: "Peacemaker Gun Course - Orb 5",
    # 130: "Peacemaker Gun Course - Orb 6",
    # 131: "Peacemaker Gun Course - Orb 7",
    # 132: "Peacemaker Gun Course - Orb 8",
    # 133: "Peacemaker Gun Course - Orb 9",
    # 134: "JET-Board Challenge - Orb 1",
    # 135: "JET-Board Challenge - Orb 2",
    # 136: "JET-Board Challenge - Orb 3",
    # 137: "JET-Board Challenge - Orb 4",
    # 138: "JET-Board Challenge - Orb 5",
    # 139: "JET-Board Challenge - Orb 6",
    # 140: "JET-Board Challenge - Orb 7",
    # 141: "JET-Board Challenge - Orb 8",
    # 142: "JET-Board Challenge - Orb 9",
    # 143: "Class 3 Race - Orb 1",
    # 144: "Class 3 Race - Orb 2",
    # 145: "Class 3 Race - Orb 3",
    # 146: "Class 3 Race - Orb 4",
    # 147: "Class 3 Race - Orb 5",
    # 148: "Class 3 Race - Orb 6",
    # 149: "Class 3 Race - Orb 7",
    # 150: "Class 3 Race - Orb 8",
    # 151: "Class 3 Race - Orb 9",
    # 152: "Class 2 Race - Orb 1",
    # 153: "Class 2 Race - Orb 2",
    # 154: "Class 2 Race - Orb 3",
    # 155: "Class 2 Race - Orb 4",
    # 156: "Class 2 Race - Orb 5",
    # 157: "Class 2 Race - Orb 6",
    # 158: "Class 2 Race - Orb 7",
    # 159: "Class 2 Race - Orb 8",
    # 160: "Class 2 Race - Orb 9",
    # 161: "Class 1 Race - Orb 1",
    # 162: "Class 1 Race - Orb 2",
    # 163: "Class 1 Race - Orb 3",
    # 164: "Class 1 Race - Orb 4",
    # 165: "Class 1 Race - Orb 5",
    # 166: "Class 1 Race - Orb 6",
    # 167: "Class 1 Race - Orb 7",
    # 168: "Class 1 Race - Orb 8",
    # 169: "Class 1 Race - Orb 9",
    # 170: "City Port Race - Orb 1",
    # 171: "City Port Race - Orb 2",
    # 172: "City Port Race - Orb 3",
    # 173: "City Port Race - Orb 4",
    # 174: "City Port Race - Orb 5",
    # 175: "City Port Race - Orb 6",
    # 176: "City Port Race - Orb 7",
    # 177: "City Port Race - Orb 8",
    # 178: "City Port Race - Orb 9",
    # 179: "Erol Race - Orb 1",
    # 180: "Erol Race - Orb 2",
    # 181: "Erol Race - Orb 3",
    # 182: "Erol Race - Orb 4",
    # 183: "Erol Race - Orb 5",
    # 184: "Erol Race - Orb 6",
    # 185: "Erol Race - Orb 7",
    # 186: "Erol Race - Orb 8",
    # 187: "Erol Race - Orb 9",
    # 188: "Reverse Class 3 Race - Orb 1",
    # 189: "Reverse Class 3 Race - Orb 2",
    # 190: "Reverse Class 3 Race - Orb 3",
    # 191: "Reverse Class 3 Race - Orb 4",
    # 192: "Reverse Class 3 Race - Orb 5",
    # 193: "Reverse Class 3 Race - Orb 6",
    # 194: "Reverse Class 3 Race - Orb 7",
    # 195: "Reverse Class 3 Race - Orb 8",
    # 196: "Reverse Class 3 Race - Orb 9",
    # 197: "Reverse Class 2 Race - Orb 1",
    # 198: "Reverse Class 2 Race - Orb 2",
    # 199: "Reverse Class 2 Race - Orb 3",
    # 200: "Reverse Class 2 Race - Orb 4",
    # 201: "Reverse Class 2 Race - Orb 5",
    # 202: "Reverse Class 2 Race - Orb 6",
    # 203: "Reverse Class 2 Race - Orb 7",
    # 204: "Reverse Class 2 Race - Orb 8",
    # 205: "Reverse Class 2 Race - Orb 9",
    # 206: "Reverse Class 1 Race - Orb 1",
    # 207: "Reverse Class 1 Race - Orb 2",
    # 208: "Reverse Class 1 Race - Orb 3",
    # 209: "Reverse Class 1 Race - Orb 4",
    # 210: "Reverse Class 1 Race - Orb 5",
    # 211: "Reverse Class 1 Race - Orb 6",
    # 212: "Reverse Class 1 Race - Orb 7",
    # 213: "Reverse Class 1 Race - Orb 8",
    # 214: "Reverse Class 1 Race - Orb 9",
    # 215: "Ring Race 1 - Orb 1",
    # 216: "Ring Race 1 - Orb 2",
    # 217: "Ring Race 1 - Orb 3",
    # 218: "Collection 1 - Orb 1",
    # 219: "Collection 1 - Orb 2",
    # 220: "Collection 1 - Orb 3",
    # 221: "Delivery to Hideout - Orb 1",
    # 222: "Delivery to Hideout - Orb 2",
    # 223: "Delivery to Hideout - Orb 3",
    # 224: "Ring Race 2 - Orb 1",
    # 225: "Ring Race 2 - Orb 2",
    # 226: "Ring Race 2 - Orb 3",
    # 227: "Shuttle Underground Fighters - Orb 1",
    # 228: "Shuttle Underground Fighters - Orb 2",
    # 229: "Shuttle Underground Fighters - Orb 3",
    # 230: "Collection 2 - Orb 1",
    # 231: "Collection 2 - Orb 2",
    # 232: "Collection 2 - Orb 3",
    # 233: "Ring Race 3 - Orb 1",
    # 234: "Ring Race 3 - Orb 2",
    # 235: "Ring Race 3 - Orb 3",
    # 236: "Destroy Blast Bots - Orb 1",
    # 237: "Destroy Blast Bots - Orb 2",
    # 238: "Destroy Blast Bots - Orb 3",
    # 239: "Collection 3 - Orb 1",
    # 240: "Collection 3 - Orb 2",
    # 241: "Collection 3 - Orb 3",
    # # Orb Search side-mission orb rewards (242-286)
    # 242: "Orb Search 1 - Orb 1",
    # 243: "Orb Search 1 - Orb 2",
    # 244: "Orb Search 1 - Orb 3",
    # 245: "Orb Search 2 - Orb 1",
    # 246: "Orb Search 2 - Orb 2",
    # 247: "Orb Search 2 - Orb 3",
    # 248: "Orb Search 3 - Orb 1",
    # 249: "Orb Search 3 - Orb 2",
    # 250: "Orb Search 3 - Orb 3",
    # 251: "Orb Search 4 - Orb 1",
    # 252: "Orb Search 4 - Orb 2",
    # 253: "Orb Search 4 - Orb 3",
    # 254: "Orb Search 5 - Orb 1",
    # 255: "Orb Search 5 - Orb 2",
    # 256: "Orb Search 5 - Orb 3",
    # 257: "Orb Search 6 - Orb 1",
    # 258: "Orb Search 6 - Orb 2",
    # 259: "Orb Search 6 - Orb 3",
    # 260: "Orb Search 7 - Orb 1",
    # 261: "Orb Search 7 - Orb 2",
    # 262: "Orb Search 7 - Orb 3",
    # 263: "Orb Search 8 - Orb 1",
    # 264: "Orb Search 8 - Orb 2",
    # 265: "Orb Search 8 - Orb 3",
    # 266: "Orb Search 9 - Orb 1",
    # 267: "Orb Search 9 - Orb 2",
    # 268: "Orb Search 9 - Orb 3",
    # 269: "Orb Search 10 - Orb 1",
    # 270: "Orb Search 10 - Orb 2",
    # 271: "Orb Search 10 - Orb 3",
    # 272: "Orb Search 11 - Orb 1",
    # 273: "Orb Search 11 - Orb 2",
    # 274: "Orb Search 11 - Orb 3",
    # 275: "Orb Search 12 - Orb 1",
    # 276: "Orb Search 12 - Orb 2",
    # 277: "Orb Search 12 - Orb 3",
    # 278: "Orb Search 13 - Orb 1",
    # 279: "Orb Search 13 - Orb 2",
    # 280: "Orb Search 13 - Orb 3",
    # 281: "Orb Search 14 - Orb 1",
    # 282: "Orb Search 14 - Orb 2",
    # 283: "Orb Search 14 - Orb 3",
    # 284: "Orb Search 15 - Orb 1",
    # 285: "Orb Search 15 - Orb 2",
    # 286: "Orb Search 15 - Orb 3",
}

orb_ids_to_orbs = {orb_id: orb for orb_id, orb in orb_names_table.items()}

def get_orb_locations(orb_checks_enabled: bool) -> dict[str, int]:
    if not orb_checks_enabled:
        return {}
    return {orb.name: orb.location_id for orb in orb_names_table.values()}