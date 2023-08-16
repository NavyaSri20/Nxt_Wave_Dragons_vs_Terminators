class Place(object):
    """A Place holds fighters and has an exit to another Place."""

    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.terminators = []  # A list of Terminators
        self.dragon = None  # A Dragon
        self.entrance = None  # A Place, newly created, so specify as None
        # Phase 1: Add an entrance to the exit
        # BEGIN 1.2
        "*** YOUR CODE HERE ***"
        if self.exit:
            self.exit.entrance = self
        # END 1.2

    def add_fighter(self, fighter):
        """Add a Fighter to this Place.

        There can be at most one Dragon in a Place, unless exactly one of them is
        a container dragon , in which case there can be two. If add_fighter
        tries to add more Dragons than is allowed, an assertion error is raised.

        There can be any number of Terminators in a Place.
        """
        if fighter.is_dragon:
            # Is the place empty?
            if self.dragon is None:
                self.dragon = fighter
            else:
                # BEGIN 3.2
                # Here self means place object
                # Check if dragon already on place is an empty container dragon
                if self.dragon.can_contain(fighter) and fighter.is_container == False:
                    self.dragon.contain_dragon(fighter)
                
                # Elif since fighter is new, so if container, it can always contain, but place dragon must not be container
                elif fighter.is_container and self.dragon.is_container == False:
                    fighter.contain_dragon(self.dragon)

                    # Since while removing the dragon, the container dragon is outer layer
                    # So colony should see container dragon and not the dragon inside
                    self.dragon = fighter
                
                else:
                    # Two incompatible Dragons in same spot, gives error
                    assert self.dragon is None, 'Two dragons in {0}'.format(self)
                # END 3.2
        else:
            self.terminators.append(fighter)
        fighter.place = self

    def remove_fighter(self, fighter):
        """Remove a FIGHTER from this Place.

        A target Dragon may either be directly in the Place, or be contained by a
        container Dragon at this place. The true DragonKing may not be removed. If
        remove_fighter tries to remove a Dragon that is not anywhere in this
        Place, an AssertionError is raised.

        A Terminator is just removed from the list of Terminators.
        """
        if fighter.is_dragon:
            # Special handling for DragonKing
            # BEGIN 4.3
            "*** YOUR CODE HERE ***"
            if (hasattr(self.dragon, 'isDragonKing') and self.dragon.isDragonKing) or (self.dragon.is_container and self.dragon.contained_dragon is not None and hasattr(self.dragon.contained_dragon, 'isDragonKing') and self.dragon.contained_dragon.isDragonKing):
                return
            # END 4.3

            # Special handling for container dragons
            if self.dragon is fighter:
                # Bodyguard was removed. Contained dragon should remain in the game
                if hasattr(self.dragon, 'is_container') and self.dragon.is_container:
                    self.dragon = self.dragon.contained_dragon
                else:
                    self.dragon = None
            else:
                # Contained dragon was removed. Bodyguard should remain
                if hasattr(self.dragon, 'is_container') and self.dragon.is_container \
                        and self.dragon.contained_dragon is fighter:
                    self.dragon.contained_dragon = None
                else:
                    assert False, '{0} is not in {1}'.format(fighter, self)
        else:
            self.terminators.remove(fighter)

        fighter.place = None

    def __str__(self):
        return self.name
