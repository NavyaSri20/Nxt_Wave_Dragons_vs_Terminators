from ..fighter import Fighter


class Terminator(Fighter):
    """A Terminator moves from place to place, following exits and stinging dragons."""

    name = 'Terminator'
    damage = 1

    # OVERRIDE CLASS ATTRIBUTES HERE
    is_watersafe = True

    def sting(self, dragon):
        """Attack a Dragon, reducing its armor by 1."""
        dragon.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Terminator's current Place to a new PLACE."""
        self.place.remove_fighter(self)
        place.add_fighter(self)

    def blocked(self):
        """Return True if this Terminator cannot advance to the next Place."""
        # BEGIN 2.4
        if self.place.dragon is not None and self.place.dragon.blocks_path == True:
            return True
        return False
        # END 2.4

    def action(self, colony):
        """A Terminator's action stings the Dragon that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The DragonColony, used to access game state information.
        """
        destination = self.place.exit
        # BEGIN 4.4
        "*** YOUR CODE HERE ***"
        if hasattr(self, 'is_scared') and self.is_scared and not hasattr(self, 'already_scared'):
            destination = self.place.entrance
        # END 4.4
        if self.blocked():
            self.sting(self.place.dragon)
        elif self.armor > 0 and destination is not None:
            self.move_to(destination)
