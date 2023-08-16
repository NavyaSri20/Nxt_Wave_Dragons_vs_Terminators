from .dragon import Dragon

class EarthDragon(Dragon):
    """EarthDragon is a dragon that does nothing each turn. However, blocks terminators due to its large armor"""

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    name = 'Earth'
    damage = 0
    food_cost = 4
    implemented = True

    # Override the __init__ method as EarthDragon has different armor that default Dragon class
    def __init__(self, armor=4):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    # Since EarthDragon does nothing, so no action method for this class


