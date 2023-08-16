from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    # Since all The thrower dragons have same food_cost
    food_cost = 3

    # Default ThrowerDragon will have min_range as 0 and max_range as INFINITY(written as float ('inf'))
    min_range = 0
    max_range = float('inf')

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        # Get the current_place of dragon
        current_place = self.place

        # Move our observation range ahead by min_range
        current_range = 0
        while current_range < self.min_range and current_place != skynet:
            current_place = current_place.entrance
            current_range += 1
        
        # Make a check if current_place has reached skynet or not
        if current_place == skynet:
            return None
        
        # Now return the first terminator within max_range
        while current_range <= self.max_range and current_place != skynet:
            if len(current_place.terminators) > 0:
                return random_or_none(current_place.terminators)
            current_place = current_place.entrance
            current_range += 1
        
        # Here? That means either no terminator found or reached the end of colony
        return None
        #return random_or_none(self.place.terminators)  # REPLACE THIS LINE
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
