from BaseClasses import Item
from .game_id import jak2_name, jak2_max

class Jak2Item(Item):
    game: str = jak2_name


class Jak2ItemData:
    id: int
    name: str
    symbol: str
    
    def __init__(self, item_id: int, name: str, symbol: str) -> None:
        self.item_id = item_id
        self.name = name
        self.symbol = symbol


# ID Range Constants for Item Classification
# These constants define the boundaries for different item types
ITEM_ID_KEY_START = 1           # Key/progression items start at ID 1
ITEM_ID_KEY_END = 33            # Key/progression items end at ID 33
ITEM_ID_FILLER_START = 34       # Filler items start at ID 34 (Dark Eco Pill)
ITEM_ID_FILLER_END = 39         # Standard filler items end at ID 39
TRAP_ID_START = 40              # Trap items start at ID 40 (Trip Trap)
TRAP_ID_END = 56                # Trap items end at ID 55

# Unified Item Table - Single source of truth for all items
# Every item is organized by classification using ID ranges defined above
item_table = {
    # ========== KEY/PROGRESSION ITEMS (IDs 1-33) ==========
    
    # Morph Gun Weapons and Upgrades (IDs 1-7)
    1: Jak2ItemData(item_id=1, name="Scatter Gun", symbol="gun-red"),
    2: Jak2ItemData(item_id=2, name="Blaster", symbol="gun-yellow"),
    3: Jak2ItemData(item_id=3, name="Vulcan Fury", symbol="gun-blue"),
    4: Jak2ItemData(item_id=4, name="Peacemaker", symbol="gun-dark"),
    5: Jak2ItemData(item_id=5, name="Morph Gun Ammo Upgrade", symbol="gun-upgrade-ammo"),
    6: Jak2ItemData(item_id=6, name="Morph Gun Fire Rate Upgrade", symbol="gun-upgrade-speed"),
    7: Jak2ItemData(item_id=7, name="Morph Gun Damage Upgrade", symbol="gun-upgrade-damage"),
    
    # Movement Items (IDs 8)
    8: Jak2ItemData(item_id=8, name="JET-Board", symbol="board"),
    
    # Dark Jak Powers (IDs 9-13)
    9: Jak2ItemData(item_id=9, name="Dark Jak", symbol="darkjak"),
    10: Jak2ItemData(item_id=10, name="Dark Bomb", symbol="darkjak-bomb0"),
    11: Jak2ItemData(item_id=11, name="Dark Blast", symbol="darkjak-bomb1"),
    12: Jak2ItemData(item_id=12, name="Dark Giant", symbol="darkjak-giant"),
    13: Jak2ItemData(item_id=13, name="Dark Invincibility", symbol="darkjak-invinc"),
    
    # Security Passes (IDs 14-19)
    14: Jak2ItemData(item_id=14, name="Red Security Pass", symbol="pass-red"),
    15: Jak2ItemData(item_id=15, name="Yellow Security Pass", symbol="pass-yellow"),
    16: Jak2ItemData(item_id=16, name="Green Security Pass", symbol="pass-green"),
    17: Jak2ItemData(item_id=17, name="Purple Security Pass", symbol="pass-purple"),
    18: Jak2ItemData(item_id=18, name="Black Security Pass", symbol="pass-black"),
    19: Jak2ItemData(item_id=19, name="Air Train Pass", symbol="pass-air-train"),
    
    # Mountain Temple Items (IDs 20-22)
    20: Jak2ItemData(item_id=20, name="Lens", symbol="lens"),
    21: Jak2ItemData(item_id=21, name="Gear", symbol="gear"),
    22: Jak2ItemData(item_id=22, name="Shard", symbol="shard"),
    
    # Miscellaneous Important Items (IDs 23-33)
    23: Jak2ItemData(item_id=23, name="Ruby Key", symbol="ruby-key"),
    24: Jak2ItemData(item_id=24, name="Heart of Mar", symbol="heart-of-mar"),
    25: Jak2ItemData(item_id=25, name="Time Map", symbol="time-map"),
    26: Jak2ItemData(item_id=26, name="Precursor Stone", symbol="precursor-stone"),
    27: Jak2ItemData(item_id=27, name="Life Seed", symbol="life-seed"),
    28: Jak2ItemData(item_id=28, name="Titan Suit", symbol="titan-suit"),
    29: Jak2ItemData(item_id=29, name="Gunpod", symbol="gun-turret"),
    30: Jak2ItemData(item_id=30, name="Seal Piece #1", symbol="seal-piece-1"),
    31: Jak2ItemData(item_id=31, name="Seal Piece #2", symbol="seal-piece-2"),
    32: Jak2ItemData(item_id=32, name="Seal Piece #3", symbol="seal-piece-3"),
    33: Jak2ItemData(item_id=33, name="Rift Rider", symbol="rift-rider"),
    
    # ========== FILLER ITEMS ==========
    # Standard Filler Items (IDs 34-39)
    34: Jak2ItemData(item_id=34, name="Dark Eco Pill", symbol="dark-eco-pill"),
    35: Jak2ItemData(item_id=35, name="Health Pack", symbol="health-pack"),
    36: Jak2ItemData(item_id=36, name="Scatter Gun Ammo", symbol="ammo-red"),
    37: Jak2ItemData(item_id=37, name="Blaster Ammo", symbol="ammo-yellow"),
    38: Jak2ItemData(item_id=38, name="Vulcan Fury Ammo", symbol="ammo-blue"),
    39: Jak2ItemData(item_id=39, name="Peacemaker Ammo", symbol="ammo-dark"),

    # Trap Items (IDs 40-56)
    # Jak 1 Traps, Reimagined for Jak 2! (IDs 40-51)
    40: Jak2ItemData(item_id=40, name="Trip Trap", symbol="trip"),
    41: Jak2ItemData(item_id=41, name="Slip Trap", symbol="ice-physics"),
    42: Jak2ItemData(item_id=42, name="Gravity Trap", symbol="the-big-apple"),
    43: Jak2ItemData(item_id=43, name="Camera Trap", symbol="caught-in-4k"),
    44: Jak2ItemData(item_id=44, name="Darkness Trap", symbol="daredevil"),
    45: Jak2ItemData(item_id=45, name="Earthquake Trap", symbol="caseoh"),
    46: Jak2ItemData(item_id=46, name="Teleport Trap", symbol="instant-transmission"),
    47: Jak2ItemData(item_id=46, name="Despair Trap", symbol="emotional-damage"),
    48: Jak2ItemData(item_id=48, name="Pacifism Trap", symbol="personal-bubble"),
    49: Jak2ItemData(item_id=49, name="Health Trap", symbol="hit-by-bus"),
    50: Jak2ItemData(item_id=50, name="Ledge Trap", symbol="rivals-of-aether"),
    51: Jak2ItemData(item_id=51, name="Mirror Trap", symbol="man-in-the-mirror"),

    # Brand New Jak 2 Traps! (IDs 52-56)
    52: Jak2ItemData(item_id=52, name="High Alert Trap", symbol="five-star"),
    53: Jak2ItemData(item_id=53, name="Ammo Trap", symbol="russian-roulette"),
    54: Jak2ItemData(item_id=54, name="Dark Trap", symbol="anger-issues"),
    55: Jak2ItemData(item_id=55, name="Hero Trap", symbol="hardcore"),
    56: Jak2ItemData(item_id=56, name="Reverse Trap", symbol="turn-right-to-go-left")
}