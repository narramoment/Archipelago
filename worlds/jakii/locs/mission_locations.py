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
    34: Jak2OrbData(orb_id=34, location_id=ORB_LOCATION_OFFSET + 34, name="Strip Mine - Orb 1",
                    rule=lambda state, player: main_mission_table[10].rule(state, player)),
    35: Jak2OrbData(orb_id=35, location_id=ORB_LOCATION_OFFSET + 35, name="Strip Mine - Orb 2",
                    rule=lambda state, player: main_mission_table[10].rule(state, player)),
    36: Jak2OrbData(orb_id=36, location_id=ORB_LOCATION_OFFSET + 36, name="Strip Mine - Orb 3",
                    rule=lambda state, player: main_mission_table[10].rule(state, player)),
    37: Jak2OrbData(orb_id=37, location_id=ORB_LOCATION_OFFSET + 37, name="Strip Mine - Orb 4",
                    rule=lambda state, player: main_mission_table[28].rule(state, player)),
    38: Jak2OrbData(orb_id=38, location_id=ORB_LOCATION_OFFSET + 38, name="Strip Mine - Orb 5",
                    rule=lambda state, player: main_mission_table[28].rule(state, player)),
    39: Jak2OrbData(orb_id=39, location_id=ORB_LOCATION_OFFSET + 39, name="Strip Mine - Orb 6",
                    rule=lambda state, player: main_mission_table[28].rule(state, player)),
    40: Jak2OrbData(orb_id=40, location_id=ORB_LOCATION_OFFSET + 40, name="Strip Mine - Orb 7",
                    rule=lambda state, player: main_mission_table[28].rule(state, player)),
    41: Jak2OrbData(orb_id=41, location_id=ORB_LOCATION_OFFSET + 41, name="Mountain Temple - Orb 1",
                    rule=lambda state, player: main_mission_table[12].rule(state, player)),
    42: Jak2OrbData(orb_id=42, location_id=ORB_LOCATION_OFFSET + 42, name="Mountain Temple - Orb 2",
                    rule=lambda state, player: main_mission_table[12].rule(state, player)),
    43: Jak2OrbData(orb_id=43, location_id=ORB_LOCATION_OFFSET + 43, name="Mountain Temple - Orb 3",
                    rule=lambda state, player: main_mission_table[13].rule(state, player)),
    44: Jak2OrbData(orb_id=44, location_id=ORB_LOCATION_OFFSET + 44, name="Mountain Temple - Orb 4",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    45: Jak2OrbData(orb_id=45, location_id=ORB_LOCATION_OFFSET + 45, name="Mountain Temple - Orb 5",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    46: Jak2OrbData(orb_id=46, location_id=ORB_LOCATION_OFFSET + 46, name="Mountain Temple - Orb 6",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    47: Jak2OrbData(orb_id=47, location_id=ORB_LOCATION_OFFSET + 47, name="Mountain Temple - Orb 7",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    48: Jak2OrbData(orb_id=48, location_id=ORB_LOCATION_OFFSET + 48, name="Mountain Temple - Orb 8",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    49: Jak2OrbData(orb_id=49, location_id=ORB_LOCATION_OFFSET + 49, name="Mountain Temple - Orb 9",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    50: Jak2OrbData(orb_id=50, location_id=ORB_LOCATION_OFFSET + 50, name="Mountain Temple - Orb 10",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    51: Jak2OrbData(orb_id=51, location_id=ORB_LOCATION_OFFSET + 51, name="Mountain Temple - Orb 11",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    52: Jak2OrbData(orb_id=52, location_id=ORB_LOCATION_OFFSET + 52, name="Mountain Temple - Orb 12",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    53: Jak2OrbData(orb_id=53, location_id=ORB_LOCATION_OFFSET + 53, name="Mountain Temple - Orb 13",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    54: Jak2OrbData(orb_id=54, location_id=ORB_LOCATION_OFFSET + 54, name="Mountain Temple - Orb 14",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    55: Jak2OrbData(orb_id=55, location_id=ORB_LOCATION_OFFSET + 55, name="Mountain Temple - Orb 15",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)),
    56: Jak2OrbData(orb_id=56, location_id=ORB_LOCATION_OFFSET + 56, name="Mountain Temple - Orb 16",
                    rule=lambda state, player: main_mission_table[14].rule(state, player)
                                               and state.has("JET-Board", player)),
    57: Jak2OrbData(orb_id=57, location_id=ORB_LOCATION_OFFSET + 57, name="Mountain Temple - Orb 17",
                    rule=lambda state, player: main_mission_table[13].rule(state, player)),
    58: Jak2OrbData(orb_id=58, location_id=ORB_LOCATION_OFFSET + 58, name="Haven Forest - Orb 1",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    59: Jak2OrbData(orb_id=59, location_id=ORB_LOCATION_OFFSET + 59, name="Haven Forest - Orb 2",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    60: Jak2OrbData(orb_id=60, location_id=ORB_LOCATION_OFFSET + 60, name="Haven Forest - Orb 3",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    61: Jak2OrbData(orb_id=61, location_id=ORB_LOCATION_OFFSET + 61, name="Haven Forest - Orb 4",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    62: Jak2OrbData(orb_id=62, location_id=ORB_LOCATION_OFFSET + 62, name="Haven Forest - Orb 5",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    63: Jak2OrbData(orb_id=63, location_id=ORB_LOCATION_OFFSET + 63, name="Haven Forest - Orb 6",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    64: Jak2OrbData(orb_id=64, location_id=ORB_LOCATION_OFFSET + 64, name="Haven Forest - Orb 7",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    65: Jak2OrbData(orb_id=65, location_id=ORB_LOCATION_OFFSET + 65, name="Haven Forest - Orb 8",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    66: Jak2OrbData(orb_id=66, location_id=ORB_LOCATION_OFFSET + 66, name="Haven Forest - Orb 9",
                    rule=lambda state, player: main_mission_table[25].rule(state, player)),
    67: Jak2OrbData(orb_id=67, location_id=ORB_LOCATION_OFFSET + 67, name="Drill Platform - Orb 1",
                    rule=lambda state, player: main_mission_table[19].rule(state, player)),
    68: Jak2OrbData(orb_id=68, location_id=ORB_LOCATION_OFFSET + 68, name="Drill Platform - Orb 2",
                    rule=lambda state, player: main_mission_table[19].rule(state, player)),
    69: Jak2OrbData(orb_id=69, location_id=ORB_LOCATION_OFFSET + 69, name="Drill Platform - Orb 3",
                    rule=lambda state, player: main_mission_table[19].rule(state, player)),
    70: Jak2OrbData(orb_id=70, location_id=ORB_LOCATION_OFFSET + 70, name="Drill Platform - Orb 4",
                    rule=lambda state, player: main_mission_table[19].rule(state, player)),
    71: Jak2OrbData(orb_id=71, location_id=ORB_LOCATION_OFFSET + 71, name="Drill Platform - Orb 5",
                    rule=lambda state, player: main_mission_table[19].rule(state, player)),
    72: Jak2OrbData(orb_id=72, location_id=ORB_LOCATION_OFFSET + 72, name="Mar's Tomb - Orb 1",
                    rule=lambda state, player: main_mission_table[41].rule(state, player)),
    73: Jak2OrbData(orb_id=73, location_id=ORB_LOCATION_OFFSET + 73, name="Mar's Tomb - Orb 2",
                    rule=lambda state, player: main_mission_table[41].rule(state, player)),
    74: Jak2OrbData(orb_id=74, location_id=ORB_LOCATION_OFFSET + 74, name="Mar's Tomb - Orb 3",
                    rule=lambda state, player: main_mission_table[41].rule(state, player)),
    75: Jak2OrbData(orb_id=75, location_id=ORB_LOCATION_OFFSET + 75, name="Mar's Tomb - Orb 4",
                    rule=lambda state, player: main_mission_table[41].rule(state, player)),
    76: Jak2OrbData(orb_id=76, location_id=ORB_LOCATION_OFFSET + 76, name="Mar's Tomb - Orb 5",
                    rule=lambda state, player: main_mission_table[41].rule(state, player)),
    77: Jak2OrbData(orb_id=77, location_id=ORB_LOCATION_OFFSET + 77, name="Dig Site - Orb 1",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    78: Jak2OrbData(orb_id=78, location_id=ORB_LOCATION_OFFSET + 78, name="Dig Site - Orb 2",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    79: Jak2OrbData(orb_id=79, location_id=ORB_LOCATION_OFFSET + 79, name="Dig Site - Orb 3",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    80: Jak2OrbData(orb_id=80, location_id=ORB_LOCATION_OFFSET + 80, name="Dig Site - Orb 4",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    81: Jak2OrbData(orb_id=81, location_id=ORB_LOCATION_OFFSET + 81, name="Dig Site - Orb 5",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    82: Jak2OrbData(orb_id=82, location_id=ORB_LOCATION_OFFSET + 82, name="Dig Site - Orb 6",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    83: Jak2OrbData(orb_id=83, location_id=ORB_LOCATION_OFFSET + 83, name="Dig Site - Orb 7",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    84: Jak2OrbData(orb_id=84, location_id=ORB_LOCATION_OFFSET + 84, name="Dig Site - Orb 8",
                    rule=lambda state, player: main_mission_table[37].rule(state, player)),
    85: Jak2OrbData(orb_id=85, location_id=ORB_LOCATION_OFFSET + 85, name="Construction Site - Orb 1",
                    rule=lambda state, player: main_mission_table[62].rule(state, player)),
    86: Jak2OrbData(orb_id=86, location_id=ORB_LOCATION_OFFSET + 86, name="Construction Site - Orb 2",
                    rule=lambda state, player: main_mission_table[62].rule(state, player)),
    87: Jak2OrbData(orb_id=87, location_id=ORB_LOCATION_OFFSET + 87, name="Under Port - Orb 1",
                    rule=lambda state, player: main_mission_table[59].rule(state, player)),
    88: Jak2OrbData(orb_id=88, location_id=ORB_LOCATION_OFFSET + 88, name="Metal Head Nest - Orb 1",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    89: Jak2OrbData(orb_id=89, location_id=ORB_LOCATION_OFFSET + 89, name="Metal Head Nest - Orb 2",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    90: Jak2OrbData(orb_id=90, location_id=ORB_LOCATION_OFFSET + 90, name="Metal Head Nest - Orb 3",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    91: Jak2OrbData(orb_id=91, location_id=ORB_LOCATION_OFFSET + 91, name="Metal Head Nest - Orb 4",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    92: Jak2OrbData(orb_id=92, location_id=ORB_LOCATION_OFFSET + 92, name="Metal Head Nest - Orb 5",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    93: Jak2OrbData(orb_id=93, location_id=ORB_LOCATION_OFFSET + 93, name="Metal Head Nest - Orb 6",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    94: Jak2OrbData(orb_id=94, location_id=ORB_LOCATION_OFFSET + 94, name="Metal Head Nest - Orb 7",
                    rule=lambda state, player: main_mission_table[63].rule(state, player)),
    # Synthetic orb-equivalents from minigames/tasks (95-241)
    95: Jak2OrbData(orb_id=95, location_id=ORB_LOCATION_OFFSET + 95, name="Onin's Game - Orb 1",
                    rule=lambda state, player: main_mission_table[39].rule(state, player)),
    96: Jak2OrbData(orb_id=96, location_id=ORB_LOCATION_OFFSET + 96, name="Onin's Game - Orb 2",
                    rule=lambda state, player: main_mission_table[39].rule(state, player)),
    97: Jak2OrbData(orb_id=97, location_id=ORB_LOCATION_OFFSET + 97, name="Onin's Game - Orb 3",
                    rule=lambda state, player: main_mission_table[39].rule(state, player)),
    98: Jak2OrbData(orb_id=98, location_id=ORB_LOCATION_OFFSET + 98, name="Scatter Gun Course - Orb 1",
                    rule=lambda state, player: main_mission_table[7].rule(state, player)),
    99: Jak2OrbData(orb_id=99, location_id=ORB_LOCATION_OFFSET + 99, name="Scatter Gun Course - Orb 2",
                    rule=lambda state, player: main_mission_table[7].rule(state, player)),
    100: Jak2OrbData(orb_id=100, location_id=ORB_LOCATION_OFFSET + 100, name="Scatter Gun Course - Orb 3",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    101: Jak2OrbData(orb_id=101, location_id=ORB_LOCATION_OFFSET + 101, name="Scatter Gun Course - Orb 4",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    102: Jak2OrbData(orb_id=102, location_id=ORB_LOCATION_OFFSET + 102, name="Scatter Gun Course - Orb 5",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    103: Jak2OrbData(orb_id=103, location_id=ORB_LOCATION_OFFSET + 103, name="Scatter Gun Course - Orb 6",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    104: Jak2OrbData(orb_id=104, location_id=ORB_LOCATION_OFFSET + 104, name="Scatter Gun Course - Orb 7",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    105: Jak2OrbData(orb_id=105, location_id=ORB_LOCATION_OFFSET + 105, name="Scatter Gun Course - Orb 8",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    106: Jak2OrbData(orb_id=106, location_id=ORB_LOCATION_OFFSET + 106, name="Scatter Gun Course - Orb 9",
                     rule=lambda state, player: main_mission_table[7].rule(state, player)),
    107: Jak2OrbData(orb_id=107, location_id=ORB_LOCATION_OFFSET + 107, name="Blaster Gun Course - Orb 1",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    108: Jak2OrbData(orb_id=108, location_id=ORB_LOCATION_OFFSET + 108, name="Blaster Gun Course - Orb 2",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    109: Jak2OrbData(orb_id=109, location_id=ORB_LOCATION_OFFSET + 109, name="Blaster Gun Course - Orb 3",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    110: Jak2OrbData(orb_id=110, location_id=ORB_LOCATION_OFFSET + 110, name="Blaster Gun Course - Orb 4",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    111: Jak2OrbData(orb_id=111, location_id=ORB_LOCATION_OFFSET + 111, name="Blaster Gun Course - Orb 5",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    112: Jak2OrbData(orb_id=112, location_id=ORB_LOCATION_OFFSET + 112, name="Blaster Gun Course - Orb 6",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    113: Jak2OrbData(orb_id=113, location_id=ORB_LOCATION_OFFSET + 113, name="Blaster Gun Course - Orb 7",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    114: Jak2OrbData(orb_id=114, location_id=ORB_LOCATION_OFFSET + 114, name="Blaster Gun Course - Orb 8",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    115: Jak2OrbData(orb_id=115, location_id=ORB_LOCATION_OFFSET + 115, name="Blaster Gun Course - Orb 9",
                     rule=lambda state, player: main_mission_table[18].rule(state, player)),
    116: Jak2OrbData(orb_id=116, location_id=ORB_LOCATION_OFFSET + 116, name="Vulcan Fury Gun Course - Orb 1",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    117: Jak2OrbData(orb_id=117, location_id=ORB_LOCATION_OFFSET + 117, name="Vulcan Fury Gun Course - Orb 2",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    118: Jak2OrbData(orb_id=118, location_id=ORB_LOCATION_OFFSET + 118, name="Vulcan Fury Gun Course - Orb 3",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    119: Jak2OrbData(orb_id=119, location_id=ORB_LOCATION_OFFSET + 119, name="Vulcan Fury Gun Course - Orb 4",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    120: Jak2OrbData(orb_id=120, location_id=ORB_LOCATION_OFFSET + 120, name="Vulcan Fury Gun Course - Orb 5",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    121: Jak2OrbData(orb_id=121, location_id=ORB_LOCATION_OFFSET + 121, name="Vulcan Fury Gun Course - Orb 6",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    122: Jak2OrbData(orb_id=122, location_id=ORB_LOCATION_OFFSET + 122, name="Vulcan Fury Gun Course - Orb 7",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    123: Jak2OrbData(orb_id=123, location_id=ORB_LOCATION_OFFSET + 123, name="Vulcan Fury Gun Course - Orb 8",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    124: Jak2OrbData(orb_id=124, location_id=ORB_LOCATION_OFFSET + 124, name="Vulcan Fury Gun Course - Orb 9",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Vulcan Fury", player)),
    125: Jak2OrbData(orb_id=125, location_id=ORB_LOCATION_OFFSET + 125, name="Peacemaker Gun Course - Orb 1",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    126: Jak2OrbData(orb_id=126, location_id=ORB_LOCATION_OFFSET + 126, name="Peacemaker Gun Course - Orb 2",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    127: Jak2OrbData(orb_id=127, location_id=ORB_LOCATION_OFFSET + 127, name="Peacemaker Gun Course - Orb 3",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    128: Jak2OrbData(orb_id=128, location_id=ORB_LOCATION_OFFSET + 128, name="Peacemaker Gun Course - Orb 4",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    129: Jak2OrbData(orb_id=129, location_id=ORB_LOCATION_OFFSET + 129, name="Peacemaker Gun Course - Orb 5",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    130: Jak2OrbData(orb_id=130, location_id=ORB_LOCATION_OFFSET + 130, name="Peacemaker Gun Course - Orb 6",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    131: Jak2OrbData(orb_id=131, location_id=ORB_LOCATION_OFFSET + 131, name="Peacemaker Gun Course - Orb 7",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    132: Jak2OrbData(orb_id=132, location_id=ORB_LOCATION_OFFSET + 132, name="Peacemaker Gun Course - Orb 8",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    133: Jak2OrbData(orb_id=133, location_id=ORB_LOCATION_OFFSET + 133, name="Peacemaker Gun Course - Orb 9",
                     rule=lambda state, player: slums_to_port(state, player) and state.has("Peacemaker", player)),
    134: Jak2OrbData(orb_id=134, location_id=ORB_LOCATION_OFFSET + 134, name="JET-Board Challenge - Orb 1",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    135: Jak2OrbData(orb_id=135, location_id=ORB_LOCATION_OFFSET + 135, name="JET-Board Challenge - Orb 2",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    136: Jak2OrbData(orb_id=136, location_id=ORB_LOCATION_OFFSET + 136, name="JET-Board Challenge - Orb 3",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    137: Jak2OrbData(orb_id=137, location_id=ORB_LOCATION_OFFSET + 137, name="JET-Board Challenge - Orb 4",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    138: Jak2OrbData(orb_id=138, location_id=ORB_LOCATION_OFFSET + 138, name="JET-Board Challenge - Orb 5",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    139: Jak2OrbData(orb_id=139, location_id=ORB_LOCATION_OFFSET + 139, name="JET-Board Challenge - Orb 6",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    140: Jak2OrbData(orb_id=140, location_id=ORB_LOCATION_OFFSET + 140, name="JET-Board Challenge - Orb 7",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    141: Jak2OrbData(orb_id=141, location_id=ORB_LOCATION_OFFSET + 141, name="JET-Board Challenge - Orb 8",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    142: Jak2OrbData(orb_id=142, location_id=ORB_LOCATION_OFFSET + 142, name="JET-Board Challenge - Orb 9",
                     rule=lambda state, player: main_mission_table[16].rule(state, player)),
    143: Jak2OrbData(orb_id=143, location_id=ORB_LOCATION_OFFSET + 143, name="Class 3 Race - Orb 1",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    144: Jak2OrbData(orb_id=144, location_id=ORB_LOCATION_OFFSET + 144, name="Class 3 Race - Orb 2",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    145: Jak2OrbData(orb_id=145, location_id=ORB_LOCATION_OFFSET + 145, name="Class 3 Race - Orb 3",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    146: Jak2OrbData(orb_id=146, location_id=ORB_LOCATION_OFFSET + 146, name="Class 3 Race - Orb 4",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    147: Jak2OrbData(orb_id=147, location_id=ORB_LOCATION_OFFSET + 147, name="Class 3 Race - Orb 5",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    148: Jak2OrbData(orb_id=148, location_id=ORB_LOCATION_OFFSET + 148, name="Class 3 Race - Orb 6",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    149: Jak2OrbData(orb_id=149, location_id=ORB_LOCATION_OFFSET + 149, name="Class 3 Race - Orb 7",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    150: Jak2OrbData(orb_id=150, location_id=ORB_LOCATION_OFFSET + 150, name="Class 3 Race - Orb 8",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    151: Jak2OrbData(orb_id=151, location_id=ORB_LOCATION_OFFSET + 151, name="Class 3 Race - Orb 9",
                     rule=lambda state, player: main_mission_table[35].rule(state, player)),
    152: Jak2OrbData(orb_id=152, location_id=ORB_LOCATION_OFFSET + 152, name="Class 2 Race - Orb 1",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    153: Jak2OrbData(orb_id=153, location_id=ORB_LOCATION_OFFSET + 153, name="Class 2 Race - Orb 2",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    154: Jak2OrbData(orb_id=154, location_id=ORB_LOCATION_OFFSET + 154, name="Class 2 Race - Orb 3",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    155: Jak2OrbData(orb_id=155, location_id=ORB_LOCATION_OFFSET + 155, name="Class 2 Race - Orb 4",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    156: Jak2OrbData(orb_id=156, location_id=ORB_LOCATION_OFFSET + 156, name="Class 2 Race - Orb 5",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    157: Jak2OrbData(orb_id=157, location_id=ORB_LOCATION_OFFSET + 157, name="Class 2 Race - Orb 6",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    158: Jak2OrbData(orb_id=158, location_id=ORB_LOCATION_OFFSET + 158, name="Class 2 Race - Orb 7",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    159: Jak2OrbData(orb_id=159, location_id=ORB_LOCATION_OFFSET + 159, name="Class 2 Race - Orb 8",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    160: Jak2OrbData(orb_id=160, location_id=ORB_LOCATION_OFFSET + 160, name="Class 2 Race - Orb 9",
                     rule=lambda state, player: main_mission_table[46].rule(state, player)),
    161: Jak2OrbData(orb_id=161, location_id=ORB_LOCATION_OFFSET + 161, name="Class 1 Race - Orb 1",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    162: Jak2OrbData(orb_id=162, location_id=ORB_LOCATION_OFFSET + 162, name="Class 1 Race - Orb 2",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    163: Jak2OrbData(orb_id=163, location_id=ORB_LOCATION_OFFSET + 163, name="Class 1 Race - Orb 3",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    164: Jak2OrbData(orb_id=164, location_id=ORB_LOCATION_OFFSET + 164, name="Class 1 Race - Orb 4",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    165: Jak2OrbData(orb_id=165, location_id=ORB_LOCATION_OFFSET + 165, name="Class 1 Race - Orb 5",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    166: Jak2OrbData(orb_id=166, location_id=ORB_LOCATION_OFFSET + 166, name="Class 1 Race - Orb 6",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    167: Jak2OrbData(orb_id=167, location_id=ORB_LOCATION_OFFSET + 167, name="Class 1 Race - Orb 7",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    168: Jak2OrbData(orb_id=168, location_id=ORB_LOCATION_OFFSET + 168, name="Class 1 Race - Orb 8",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    169: Jak2OrbData(orb_id=169, location_id=ORB_LOCATION_OFFSET + 169, name="Class 1 Race - Orb 9",
                     rule=lambda state, player: main_mission_table[54].rule(state, player)),
    170: Jak2OrbData(orb_id=170, location_id=ORB_LOCATION_OFFSET + 170, name="City Port Race - Orb 1",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    171: Jak2OrbData(orb_id=171, location_id=ORB_LOCATION_OFFSET + 171, name="City Port Race - Orb 2",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    172: Jak2OrbData(orb_id=172, location_id=ORB_LOCATION_OFFSET + 172, name="City Port Race - Orb 3",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    173: Jak2OrbData(orb_id=173, location_id=ORB_LOCATION_OFFSET + 173, name="City Port Race - Orb 4",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    174: Jak2OrbData(orb_id=174, location_id=ORB_LOCATION_OFFSET + 174, name="City Port Race - Orb 5",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    175: Jak2OrbData(orb_id=175, location_id=ORB_LOCATION_OFFSET + 175, name="City Port Race - Orb 6",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    176: Jak2OrbData(orb_id=176, location_id=ORB_LOCATION_OFFSET + 176, name="City Port Race - Orb 7",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    177: Jak2OrbData(orb_id=177, location_id=ORB_LOCATION_OFFSET + 177, name="City Port Race - Orb 8",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    178: Jak2OrbData(orb_id=178, location_id=ORB_LOCATION_OFFSET + 178, name="City Port Race - Orb 9",
                     rule=lambda state, player: side_mission_table[126].rule(state, player)),
    179: Jak2OrbData(orb_id=179, location_id=ORB_LOCATION_OFFSET + 179, name="Erol Race - Orb 1",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    180: Jak2OrbData(orb_id=180, location_id=ORB_LOCATION_OFFSET + 180, name="Erol Race - Orb 2",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    181: Jak2OrbData(orb_id=181, location_id=ORB_LOCATION_OFFSET + 181, name="Erol Race - Orb 3",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    182: Jak2OrbData(orb_id=182, location_id=ORB_LOCATION_OFFSET + 182, name="Erol Race - Orb 4",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    183: Jak2OrbData(orb_id=183, location_id=ORB_LOCATION_OFFSET + 183, name="Erol Race - Orb 5",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    184: Jak2OrbData(orb_id=184, location_id=ORB_LOCATION_OFFSET + 184, name="Erol Race - Orb 6",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    185: Jak2OrbData(orb_id=185, location_id=ORB_LOCATION_OFFSET + 185, name="Erol Race - Orb 7",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    186: Jak2OrbData(orb_id=186, location_id=ORB_LOCATION_OFFSET + 186, name="Erol Race - Orb 8",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    187: Jak2OrbData(orb_id=187, location_id=ORB_LOCATION_OFFSET + 187, name="Erol Race - Orb 9",
                     rule=lambda state, player: side_mission_table[125].rule(state, player)),
    188: Jak2OrbData(orb_id=188, location_id=ORB_LOCATION_OFFSET + 188, name="Reverse Class 3 Race - Orb 1",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    189: Jak2OrbData(orb_id=189, location_id=ORB_LOCATION_OFFSET + 189, name="Reverse Class 3 Race - Orb 2",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    190: Jak2OrbData(orb_id=190, location_id=ORB_LOCATION_OFFSET + 190, name="Reverse Class 3 Race - Orb 3",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    191: Jak2OrbData(orb_id=191, location_id=ORB_LOCATION_OFFSET + 191, name="Reverse Class 3 Race - Orb 4",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    192: Jak2OrbData(orb_id=192, location_id=ORB_LOCATION_OFFSET + 192, name="Reverse Class 3 Race - Orb 5",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    193: Jak2OrbData(orb_id=193, location_id=ORB_LOCATION_OFFSET + 193, name="Reverse Class 3 Race - Orb 6",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    194: Jak2OrbData(orb_id=194, location_id=ORB_LOCATION_OFFSET + 194, name="Reverse Class 3 Race - Orb 7",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    195: Jak2OrbData(orb_id=195, location_id=ORB_LOCATION_OFFSET + 195, name="Reverse Class 3 Race - Orb 8",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    196: Jak2OrbData(orb_id=196, location_id=ORB_LOCATION_OFFSET + 196, name="Reverse Class 3 Race - Orb 9",
                     rule=lambda state, player: side_mission_table[131].rule(state, player)),
    197: Jak2OrbData(orb_id=197, location_id=ORB_LOCATION_OFFSET + 197, name="Reverse Class 2 Race - Orb 1",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    198: Jak2OrbData(orb_id=198, location_id=ORB_LOCATION_OFFSET + 198, name="Reverse Class 2 Race - Orb 2",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    199: Jak2OrbData(orb_id=199, location_id=ORB_LOCATION_OFFSET + 199, name="Reverse Class 2 Race - Orb 3",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    200: Jak2OrbData(orb_id=200, location_id=ORB_LOCATION_OFFSET + 200, name="Reverse Class 2 Race - Orb 4",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    201: Jak2OrbData(orb_id=201, location_id=ORB_LOCATION_OFFSET + 201, name="Reverse Class 2 Race - Orb 5",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    202: Jak2OrbData(orb_id=202, location_id=ORB_LOCATION_OFFSET + 202, name="Reverse Class 2 Race - Orb 6",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    203: Jak2OrbData(orb_id=203, location_id=ORB_LOCATION_OFFSET + 203, name="Reverse Class 2 Race - Orb 7",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    204: Jak2OrbData(orb_id=204, location_id=ORB_LOCATION_OFFSET + 204, name="Reverse Class 2 Race - Orb 8",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    205: Jak2OrbData(orb_id=205, location_id=ORB_LOCATION_OFFSET + 205, name="Reverse Class 2 Race - Orb 9",
                     rule=lambda state, player: side_mission_table[132].rule(state, player)),
    206: Jak2OrbData(orb_id=206, location_id=ORB_LOCATION_OFFSET + 206, name="Reverse Class 1 Race - Orb 1",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    207: Jak2OrbData(orb_id=207, location_id=ORB_LOCATION_OFFSET + 207, name="Reverse Class 1 Race - Orb 2",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    208: Jak2OrbData(orb_id=208, location_id=ORB_LOCATION_OFFSET + 208, name="Reverse Class 1 Race - Orb 3",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    209: Jak2OrbData(orb_id=209, location_id=ORB_LOCATION_OFFSET + 209, name="Reverse Class 1 Race - Orb 4",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    210: Jak2OrbData(orb_id=210, location_id=ORB_LOCATION_OFFSET + 210, name="Reverse Class 1 Race - Orb 5",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    211: Jak2OrbData(orb_id=211, location_id=ORB_LOCATION_OFFSET + 211, name="Reverse Class 1 Race - Orb 6",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    212: Jak2OrbData(orb_id=212, location_id=ORB_LOCATION_OFFSET + 212, name="Reverse Class 1 Race - Orb 7",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    213: Jak2OrbData(orb_id=213, location_id=ORB_LOCATION_OFFSET + 213, name="Reverse Class 1 Race - Orb 8",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    214: Jak2OrbData(orb_id=214, location_id=ORB_LOCATION_OFFSET + 214, name="Reverse Class 1 Race - Orb 9",
                     rule=lambda state, player: side_mission_table[133].rule(state, player)),
    215: Jak2OrbData(orb_id=215, location_id=ORB_LOCATION_OFFSET + 215, name="Ring Race 1 - Orb 1",
                     rule=lambda state, player: side_mission_table[116].rule(state, player)),
    216: Jak2OrbData(orb_id=216, location_id=ORB_LOCATION_OFFSET + 216, name="Ring Race 1 - Orb 2",
                     rule=lambda state, player: side_mission_table[116].rule(state, player)),
    217: Jak2OrbData(orb_id=217, location_id=ORB_LOCATION_OFFSET + 217, name="Ring Race 1 - Orb 3",
                     rule=lambda state, player: side_mission_table[116].rule(state, player)),
    218: Jak2OrbData(orb_id=218, location_id=ORB_LOCATION_OFFSET + 218, name="Collection 1 - Orb 1",
                     rule=lambda state, player: side_mission_table[119].rule(state, player)),
    219: Jak2OrbData(orb_id=219, location_id=ORB_LOCATION_OFFSET + 219, name="Collection 1 - Orb 2",
                     rule=lambda state, player: side_mission_table[119].rule(state, player)),
    220: Jak2OrbData(orb_id=220, location_id=ORB_LOCATION_OFFSET + 220, name="Collection 1 - Orb 3",
                     rule=lambda state, player: side_mission_table[119].rule(state, player)),
    221: Jak2OrbData(orb_id=221, location_id=ORB_LOCATION_OFFSET + 221, name="Delivery to Hideout - Orb 1",
                     rule=lambda state, player: side_mission_table[122].rule(state, player)),
    222: Jak2OrbData(orb_id=222, location_id=ORB_LOCATION_OFFSET + 222, name="Delivery to Hideout - Orb 2",
                     rule=lambda state, player: side_mission_table[122].rule(state, player)),
    223: Jak2OrbData(orb_id=223, location_id=ORB_LOCATION_OFFSET + 223, name="Delivery to Hideout - Orb 3",
                     rule=lambda state, player: side_mission_table[122].rule(state, player)),
    224: Jak2OrbData(orb_id=224, location_id=ORB_LOCATION_OFFSET + 224, name="Ring Race 2 - Orb 1",
                     rule=lambda state, player: side_mission_table[117].rule(state, player)),
    225: Jak2OrbData(orb_id=225, location_id=ORB_LOCATION_OFFSET + 225, name="Ring Race 2 - Orb 2",
                     rule=lambda state, player: side_mission_table[117].rule(state, player)),
    226: Jak2OrbData(orb_id=226, location_id=ORB_LOCATION_OFFSET + 226, name="Ring Race 2 - Orb 3",
                     rule=lambda state, player: side_mission_table[117].rule(state, player)),
    227: Jak2OrbData(orb_id=227, location_id=ORB_LOCATION_OFFSET + 227, name="Shuttle Underground Fighters - Orb 1",
                     rule=lambda state, player: side_mission_table[123].rule(state, player)),
    228: Jak2OrbData(orb_id=228, location_id=ORB_LOCATION_OFFSET + 228, name="Shuttle Underground Fighters - Orb 2",
                     rule=lambda state, player: side_mission_table[123].rule(state, player)),
    229: Jak2OrbData(orb_id=229, location_id=ORB_LOCATION_OFFSET + 229, name="Shuttle Underground Fighters - Orb 3",
                     rule=lambda state, player: side_mission_table[123].rule(state, player)),
    230: Jak2OrbData(orb_id=230, location_id=ORB_LOCATION_OFFSET + 230, name="Collection 2 - Orb 1",
                     rule=lambda state, player: side_mission_table[120].rule(state, player)),
    231: Jak2OrbData(orb_id=231, location_id=ORB_LOCATION_OFFSET + 231, name="Collection 2 - Orb 2",
                     rule=lambda state, player: side_mission_table[120].rule(state, player)),
    232: Jak2OrbData(orb_id=232, location_id=ORB_LOCATION_OFFSET + 232, name="Collection 2 - Orb 3",
                     rule=lambda state, player: side_mission_table[120].rule(state, player)),
    233: Jak2OrbData(orb_id=233, location_id=ORB_LOCATION_OFFSET + 233, name="Ring Race 3 - Orb 1",
                     rule=lambda state, player: side_mission_table[118].rule(state, player)),
    234: Jak2OrbData(orb_id=234, location_id=ORB_LOCATION_OFFSET + 234, name="Ring Race 3 - Orb 2",
                     rule=lambda state, player: side_mission_table[118].rule(state, player)),
    235: Jak2OrbData(orb_id=235, location_id=ORB_LOCATION_OFFSET + 235, name="Ring Race 3 - Orb 3",
                     rule=lambda state, player: side_mission_table[118].rule(state, player)),
    236: Jak2OrbData(orb_id=236, location_id=ORB_LOCATION_OFFSET + 236, name="Destroy Blast Bots - Orb 1",
                     rule=lambda state, player: side_mission_table[124].rule(state, player)),
    237: Jak2OrbData(orb_id=237, location_id=ORB_LOCATION_OFFSET + 237, name="Destroy Blast Bots - Orb 2",
                     rule=lambda state, player: side_mission_table[124].rule(state, player)),
    238: Jak2OrbData(orb_id=238, location_id=ORB_LOCATION_OFFSET + 238, name="Destroy Blast Bots - Orb 3",
                     rule=lambda state, player: side_mission_table[123].rule(state, player)),
    239: Jak2OrbData(orb_id=239, location_id=ORB_LOCATION_OFFSET + 239, name="Collection 3 - Orb 1",
                     rule=lambda state, player: side_mission_table[121].rule(state, player)),
    240: Jak2OrbData(orb_id=240, location_id=ORB_LOCATION_OFFSET + 240, name="Collection 3 - Orb 2",
                     rule=lambda state, player: side_mission_table[121].rule(state, player)),
    241: Jak2OrbData(orb_id=241, location_id=ORB_LOCATION_OFFSET + 241, name="Collection 3 - Orb 3",
                     rule=lambda state, player: side_mission_table[121].rule(state, player)),
    # Orb Search side-mission orb rewards (242-286)
    242: Jak2OrbData(orb_id=242, location_id=ORB_LOCATION_OFFSET + 242, name="Orb Search 1 - Orb 1",
                     rule=lambda state, player: side_mission_table[101].rule(state, player)),
    243: Jak2OrbData(orb_id=243, location_id=ORB_LOCATION_OFFSET + 243, name="Orb Search 1 - Orb 2",
                     rule=lambda state, player: side_mission_table[101].rule(state, player)),
    244: Jak2OrbData(orb_id=244, location_id=ORB_LOCATION_OFFSET + 244, name="Orb Search 1 - Orb 3",
                     rule=lambda state, player: side_mission_table[101].rule(state, player)),
    245: Jak2OrbData(orb_id=245, location_id=ORB_LOCATION_OFFSET + 245, name="Orb Search 2 - Orb 1",
                     rule=lambda state, player: side_mission_table[102].rule(state, player)),
    246: Jak2OrbData(orb_id=246, location_id=ORB_LOCATION_OFFSET + 246, name="Orb Search 2 - Orb 2",
                     rule=lambda state, player: side_mission_table[102].rule(state, player)),
    247: Jak2OrbData(orb_id=247, location_id=ORB_LOCATION_OFFSET + 247, name="Orb Search 2 - Orb 3",
                     rule=lambda state, player: side_mission_table[102].rule(state, player)),
    248: Jak2OrbData(orb_id=248, location_id=ORB_LOCATION_OFFSET + 248, name="Orb Search 3 - Orb 1",
                     rule=lambda state, player: side_mission_table[103].rule(state, player)),
    249: Jak2OrbData(orb_id=249, location_id=ORB_LOCATION_OFFSET + 249, name="Orb Search 3 - Orb 2",
                     rule=lambda state, player: side_mission_table[103].rule(state, player)),
    250: Jak2OrbData(orb_id=250, location_id=ORB_LOCATION_OFFSET + 250, name="Orb Search 3 - Orb 3",
                     rule=lambda state, player: side_mission_table[103].rule(state, player)),
    251: Jak2OrbData(orb_id=251, location_id=ORB_LOCATION_OFFSET + 251, name="Orb Search 4 - Orb 1",
                     rule=lambda state, player: side_mission_table[104].rule(state, player)),
    252: Jak2OrbData(orb_id=252, location_id=ORB_LOCATION_OFFSET + 252, name="Orb Search 4 - Orb 2",
                     rule=lambda state, player: side_mission_table[104].rule(state, player)),
    253: Jak2OrbData(orb_id=253, location_id=ORB_LOCATION_OFFSET + 253, name="Orb Search 4 - Orb 3",
                     rule=lambda state, player: side_mission_table[104].rule(state, player)),
    254: Jak2OrbData(orb_id=254, location_id=ORB_LOCATION_OFFSET + 254, name="Orb Search 5 - Orb 1",
                     rule=lambda state, player: side_mission_table[105].rule(state, player)),
    255: Jak2OrbData(orb_id=255, location_id=ORB_LOCATION_OFFSET + 255, name="Orb Search 5 - Orb 2",
                     rule=lambda state, player: side_mission_table[105].rule(state, player)),
    256: Jak2OrbData(orb_id=256, location_id=ORB_LOCATION_OFFSET + 256, name="Orb Search 5 - Orb 3",
                     rule=lambda state, player: side_mission_table[105].rule(state, player)),
    257: Jak2OrbData(orb_id=257, location_id=ORB_LOCATION_OFFSET + 257, name="Orb Search 6 - Orb 1",
                     rule=lambda state, player: side_mission_table[106].rule(state, player)),
    258: Jak2OrbData(orb_id=258, location_id=ORB_LOCATION_OFFSET + 258, name="Orb Search 6 - Orb 2",
                     rule=lambda state, player: side_mission_table[106].rule(state, player)),
    259: Jak2OrbData(orb_id=259, location_id=ORB_LOCATION_OFFSET + 259, name="Orb Search 6 - Orb 3",
                     rule=lambda state, player: side_mission_table[106].rule(state, player)),
    260: Jak2OrbData(orb_id=260, location_id=ORB_LOCATION_OFFSET + 260, name="Orb Search 7 - Orb 1",
                     rule=lambda state, player: side_mission_table[107].rule(state, player)),
    261: Jak2OrbData(orb_id=261, location_id=ORB_LOCATION_OFFSET + 261, name="Orb Search 7 - Orb 2",
                     rule=lambda state, player: side_mission_table[107].rule(state, player)),
    262: Jak2OrbData(orb_id=262, location_id=ORB_LOCATION_OFFSET + 262, name="Orb Search 7 - Orb 3",
                     rule=lambda state, player: side_mission_table[107].rule(state, player)),
    263: Jak2OrbData(orb_id=263, location_id=ORB_LOCATION_OFFSET + 263, name="Orb Search 8 - Orb 1",
                     rule=lambda state, player: side_mission_table[108].rule(state, player)),
    264: Jak2OrbData(orb_id=264, location_id=ORB_LOCATION_OFFSET + 264, name="Orb Search 8 - Orb 2",
                     rule=lambda state, player: side_mission_table[108].rule(state, player)),
    265: Jak2OrbData(orb_id=265, location_id=ORB_LOCATION_OFFSET + 265, name="Orb Search 8 - Orb 3",
                     rule=lambda state, player: side_mission_table[108].rule(state, player)),
    266: Jak2OrbData(orb_id=266, location_id=ORB_LOCATION_OFFSET + 266, name="Orb Search 9 - Orb 1",
                     rule=lambda state, player: side_mission_table[109].rule(state, player)),
    267: Jak2OrbData(orb_id=267, location_id=ORB_LOCATION_OFFSET + 267, name="Orb Search 9 - Orb 2",
                     rule=lambda state, player: side_mission_table[109].rule(state, player)),
    268: Jak2OrbData(orb_id=268, location_id=ORB_LOCATION_OFFSET + 268, name="Orb Search 9 - Orb 3",
                     rule=lambda state, player: side_mission_table[109].rule(state, player)),
    269: Jak2OrbData(orb_id=269, location_id=ORB_LOCATION_OFFSET + 269, name="Orb Search 10 - Orb 1",
                     rule=lambda state, player: side_mission_table[110].rule(state, player)),
    270: Jak2OrbData(orb_id=270, location_id=ORB_LOCATION_OFFSET + 270, name="Orb Search 10 - Orb 2",
                     rule=lambda state, player: side_mission_table[110].rule(state, player)),
    271: Jak2OrbData(orb_id=271, location_id=ORB_LOCATION_OFFSET + 271, name="Orb Search 10 - Orb 3",
                     rule=lambda state, player: side_mission_table[110].rule(state, player)),
    272: Jak2OrbData(orb_id=272, location_id=ORB_LOCATION_OFFSET + 272, name="Orb Search 11 - Orb 1",
                     rule=lambda state, player: side_mission_table[111].rule(state, player)),
    273: Jak2OrbData(orb_id=273, location_id=ORB_LOCATION_OFFSET + 273, name="Orb Search 11 - Orb 2",
                     rule=lambda state, player: side_mission_table[111].rule(state, player)),
    274: Jak2OrbData(orb_id=274, location_id=ORB_LOCATION_OFFSET + 274, name="Orb Search 11 - Orb 3",
                     rule=lambda state, player: side_mission_table[111].rule(state, player)),
    275: Jak2OrbData(orb_id=275, location_id=ORB_LOCATION_OFFSET + 275, name="Orb Search 12 - Orb 1",
                     rule=lambda state, player: side_mission_table[112].rule(state, player)),
    276: Jak2OrbData(orb_id=276, location_id=ORB_LOCATION_OFFSET + 276, name="Orb Search 12 - Orb 2",
                     rule=lambda state, player: side_mission_table[112].rule(state, player)),
    277: Jak2OrbData(orb_id=277, location_id=ORB_LOCATION_OFFSET + 277, name="Orb Search 12 - Orb 3",
                     rule=lambda state, player: side_mission_table[112].rule(state, player)),
    278: Jak2OrbData(orb_id=278, location_id=ORB_LOCATION_OFFSET + 278, name="Orb Search 13 - Orb 1",
                     rule=lambda state, player: side_mission_table[113].rule(state, player)),
    279: Jak2OrbData(orb_id=279, location_id=ORB_LOCATION_OFFSET + 279, name="Orb Search 13 - Orb 2",
                     rule=lambda state, player: side_mission_table[113].rule(state, player)),
    280: Jak2OrbData(orb_id=280, location_id=ORB_LOCATION_OFFSET + 280, name="Orb Search 13 - Orb 3",
                     rule=lambda state, player: side_mission_table[113].rule(state, player)),
    281: Jak2OrbData(orb_id=281, location_id=ORB_LOCATION_OFFSET + 281, name="Orb Search 14 - Orb 1",
                     rule=lambda state, player: side_mission_table[114].rule(state, player)),
    282: Jak2OrbData(orb_id=282, location_id=ORB_LOCATION_OFFSET + 282, name="Orb Search 14 - Orb 2",
                     rule=lambda state, player: side_mission_table[114].rule(state, player)),
    283: Jak2OrbData(orb_id=283, location_id=ORB_LOCATION_OFFSET + 283, name="Orb Search 14 - Orb 3",
                     rule=lambda state, player: side_mission_table[114].rule(state, player)),
    284: Jak2OrbData(orb_id=284, location_id=ORB_LOCATION_OFFSET + 284, name="Orb Search 15 - Orb 1",
                     rule=lambda state, player: side_mission_table[115].rule(state, player)),
    285: Jak2OrbData(orb_id=285, location_id=ORB_LOCATION_OFFSET + 285, name="Orb Search 15 - Orb 2",
                     rule=lambda state, player: side_mission_table[115].rule(state, player)),
    286: Jak2OrbData(orb_id=286, location_id=ORB_LOCATION_OFFSET + 286, name="Orb Search 15 - Orb 3",
                     rule=lambda state, player: side_mission_table[115].rule(state, player)),
}

orb_ids_to_orbs = {orb_id: orb for orb_id, orb in orb_names_table.items()}

def get_orb_locations(orb_checks_enabled: bool) -> dict[str, int]:
    if not orb_checks_enabled:
        return {}
    return {orb.name: orb.location_id for orb in orb_names_table.values()}