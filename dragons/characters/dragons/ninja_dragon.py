from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 5
    armor = 1

    # BEGIN 2.4
    blocks_path = False # Ninja Dragon does not block path
    implemented = True  # Change to True to view in the GUI
    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        terminator_list_copy = [i for i in self.place.terminators]
        for terminator in terminator_list_copy:
            terminator.reduce_armor(self.damage)
