from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    food_cost = 5
    #armor = 3 Armor is a instance attribute
    implemented = True  # Change to True to view in the GUI

    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    # Since FireDragon has different actions on armor reduction, overwrite this method from Fighter Class
    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        "*** YOUR CODE HERE ***"
        # Reduce armor by amount
        self.armor -= amount

        # Hint Suggest to iterate over a shallow copy of list of terminators present in self.place
        terminator_list_copy = [i for i in self.place.terminators]

        # Check if fire dragon is dead
        if self.armor <= 0:
            for terminator in terminator_list_copy:
                # Reduce armor of terminator by 'damage' that dragons deals on death
                # As well as Reflected damage
                terminator.reduce_armor(amount + self.damage)
            
            # Since dragon is dead, remove it
            self.place.remove_fighter(self)
            self.death_callback()
        
        else:
            for terminator in terminator_list_copy:
                # Reduce terminator armor by 'Amount' as Reflected damage
                terminator.reduce_armor(amount)

        
