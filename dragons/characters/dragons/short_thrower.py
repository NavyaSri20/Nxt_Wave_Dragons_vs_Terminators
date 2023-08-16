from .thrower_dragon import ThrowerDragon


class ShortThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at most 3 places away."""

    name = 'Short'
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2
    
    # BEGIN 2.1
    min_range = 0
    max_range = 3
    implemented = True  # Change to True to view in the GUI
    # END 2.1
