from ..fighter import Fighter


class Dragon(Fighter):
    """A Dragon occupies a place and does work for the colony."""
    is_dragon = True
    blocks_path = True  # Phase 2.4 for Ninja Dragon
    implemented = False  # Only implemented Dragon classes should be instantiated
    is_container = False # Should be true only for Container Dragons
    is_buffed = False # Is set to true when a DragonKing buffs the dragon
    food_cost = 0

    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, armor=1):
        """Create a Dragon with a ARMOR quantity."""
        Fighter.__init__(self, armor)

    def can_contain(self, other):
        return False

    def contain_dragon(self, other):
        assert False, "{0} cannot contain a dragon".format(self)

    def remove_dragon(self, other):
        assert False, "{0} cannot contain a dragon".format(self)

    def add_to(self, place):
        if place.dragon is None:
            place.dragon = self
        else:
            # BEGIN 3.1
            assert place.dragon is None, 'Two dragons in {0}'.format(place)
            # END 3.1
        Fighter.add_to(self, place)

    def remove_from(self, place):
        if place.dragon is self:
            place.dragon = None
        elif place.dragon is None:
            assert False, '{0} is not in {1}'.format(self, place)
        else:
            # container or other situation
            place.dragon.remove_dragon(self)
        Fighter.remove_from(self, place)
