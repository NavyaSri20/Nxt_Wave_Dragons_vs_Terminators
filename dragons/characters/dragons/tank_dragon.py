from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    food_cost = 6
    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        # Reduce armor of all terminators by 1 in the same place
        terminator_list_copy = [i for i in self.place.terminators]
        for terminator in terminator_list_copy:
            terminator.reduce_armor(self.damage)
        
        # Now perform the action of Bodyguard_dragon, as it contains action for dragon contained inside it
        # Since it's a super class of TankDragon, we can use super() to call action method
        super().action(colony)

        # Rest all is taken care by Super classes
        # END 3.3

