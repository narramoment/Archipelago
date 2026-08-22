from dataclasses import dataclass
from functools import cached_property
from Options import PerGameCommonOptions, StartInventoryPool, Choice, Range, OptionCounter, Toggle
from .items import item_table, TRAP_ID_START, TRAP_ID_END


class CompletionCondition(Choice):
    """Set your goal for completion!"""
    display_name = "Completion Condition"
    option_complete_specific_mission = 1
    option_complete_number_of_missions = 2
    default = 1


class SpecificMissionForCompletion(Choice):
    """Set the specific mission to complete for the "Complete Specific Mission" completion condition."""
    display_name = "Specific Mission for Completion"
    option_unlock_mar_tomb = 40
    option_defeat_baron_at_palace = 22
    option_defeat_baron_in_tomb = 43
    option_defeat_metal_kor = 65
    default = 65


class NumberOfMissionsForCompletion(Range):
    """Set the number of missions to complete for the "Complete Number of Missions" completion condition."""
    display_name = "Number of Missions for Completion"
    range_start = 5
    range_end = 92
    default = 65


class PercentOfFillerItemsReplacedWithTraps(Range):
    """
    Set the percentage of filler to be replaced with traps. This does not affect your progressive items.

    If this value is greater than the number of filler items, then they will all be replaced with traps.
    """
    display_name = "Percent of Filler Items Replaced with Traps"
    range_start = 0
    range_end = 100
    default = 0


class TrapEffectDuration(Range):
    """
    The length of time, in seconds, that a trap will last.
    """
    display_name = "Trap Effect Duration"
    range_start = 5
    range_end = 60
    default = 30


class TrapWeights(OptionCounter):
    """
    The list of traps, and corresponding weights that will be randomly added to the item pool. A trap with a weight of
    10 is twice as likely to appear than a trap with a weight of 5. Set a trap with a weight of 0 to prevent that trap
    appearing altogether. If all weights are 0, no traps are created, overriding the value of "Percent of Filler Items
    Replaced with Traps".
    """
    display_name = "Trap Weights"
    min = 0

    # Use trap names as keys
    traps = [trap for key, trap in item_table.items() if TRAP_ID_START <= key <= TRAP_ID_END]

    default = {trap.name: 1 for trap in traps}
    valid_keys = sorted({trap.name for trap in traps})

    @cached_property
    def weighted_pair(self) -> tuple[list[str], list[int]]:
        return list(self.value.keys()), list(self.value.values())


class RandomizeOracleCost(Toggle):
    """If enabled, the Skull Gem cost to unlock each Oracle Dark Jak power will be randomized per stage."""
    display_name = "Randomize Oracle Cost"


class OracleCostLevel0(Range):
    """Skull Gem cost for the 1st Oracle trial (Dark Bomb) (vanilla: 25). Only used if Randomize Oracle Cost is enabled."""
    display_name = "Oracle Cost - Dark Bomb"
    range_start = 0
    range_end = 100
    default = 25


class OracleCostLevel1(Range):
    """Skull Gem cost for the 2nd Oracle trial (Dark Blast) (vanilla: 200). Only used if Randomize Oracle Cost is enabled."""
    display_name = "Oracle Cost - Dark Blast"
    range_start = 0
    range_end = 100
    default = 200


class OracleCostLevel2(Range):
    """Skull Gem cost for the 3rd Oracle trial (Dark Invincibility) (vanilla: 200). Only used if Randomize Oracle Cost is enabled."""
    display_name = "Oracle Cost - Dark Invincibility"
    range_start = 0
    range_end = 100
    default = 200


class OracleCostLevel3(Range):
    """Skull Gem cost for the 4th Oracle trial (Dark Giant) (vanilla: 100). Only used if Randomize Oracle Cost is enabled."""
    display_name = "Oracle Cost - Dark Giant"
    range_start = 0
    range_end = 100
    default = 100


@dataclass
class JakIIOptions(PerGameCommonOptions):
    jak_2_completion_condition: CompletionCondition
    specific_mission_for_completion: SpecificMissionForCompletion
    number_of_missions_for_completion: NumberOfMissionsForCompletion
    percent_filler_replaced_with_traps: PercentOfFillerItemsReplacedWithTraps
    trap_effect_duration: TrapEffectDuration
    trap_weights: TrapWeights
    randomize_oracle_cost: RandomizeOracleCost
    oracle_cost_level0: OracleCostLevel0
    oracle_cost_level1: OracleCostLevel1
    oracle_cost_level2: OracleCostLevel2
    oracle_cost_level3: OracleCostLevel3
    start_inventory_from_pool: StartInventoryPool