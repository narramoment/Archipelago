import Utils

# this is no longer the only thing. that's not it :(
jak2_name = "Jak II"

# Maximum base item ID, used for filler item offset calculations
# Current highest key item ID is 33, so we use a higher base for future expansion
jak2_max = 100000

# The executable name of the GOAL Kernel.
jak2_gk = "gk" + (".exe" if Utils.is_windows else "")

# The executable name of the GOAL Compiler.
jak2_goalc = "goalc" + (".exe" if Utils.is_windows else "")
