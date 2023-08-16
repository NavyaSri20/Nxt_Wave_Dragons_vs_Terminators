from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    food_cost = 10

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        fighters = {}
        distance = 0
        current_place = self.place
        # First check if Laser Dragon is inside a container. Also, check terminators in same place
        if current_place.dragon is not None and current_place.dragon != self:
            fighters[current_place.dragon] = distance
        fighters_list_copy = dict([(i, distance) for i in current_place.terminators])
        fighters.update(fighters_list_copy)

        # Keep moving places ahead and check for fighters
        current_place = current_place.entrance
        distance += 1
        while current_place != skynet:
            if current_place.dragon is not None:
                fighters[current_place.dragon] = distance
            fighters_list_copy = dict([(i, distance) for i in current_place.terminators])
            fighters.update(fighters_list_copy)
            current_place = current_place.entrance
            distance += 1
        return fighters
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        return 2.0 - 0.2 * distance - 0.05 * self.fighters_shot
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
