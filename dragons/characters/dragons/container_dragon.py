from .dragon import Dragon
from ..fighter import Fighter


class ContainerDragon(Dragon):
    def __init__(self, *args, **kwargs):
        Dragon.__init__(self, *args, **kwargs)
        self.contained_dragon = None

    def can_contain(self, other):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if self.contained_dragon == None and other.is_container == False:
            return True
        return False
        # END 3.2

    def contain_dragon(self, dragon):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        self.contained_dragon = dragon
        # END 3.2

    def remove_dragon(self, dragon):
        if self.contained_dragon is not dragon:
            assert False, "{} does not contain {}".format(self, dragon)
        self.contained_dragon = None

    def remove_from(self, place):
        # Special handling for container dragons
        if place.dragon is self:
            # Container was removed. Contained dragon should remain in the game
            place.dragon = place.dragon.contained_dragon
            Fighter.remove_from(self, place)
        else:
            # default to normal behavior
            Dragon.remove_from(self, place)

    def action(self, colony):
        # BEGIN 3.2
        "*** YOUR CODE HERE ***"
        if self.contained_dragon is not None:
            return self.contained_dragon.action(colony)
