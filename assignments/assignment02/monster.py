import random

class Monster():
    def __init__(character):
        character.combat_strength = random.randint(1, 10)
        character.health_points = random.randint(1, 10)

    @property
    def get_combat_strength(self):
        return self.combat_strength

    @get_combat_strength.setter
    def set_combat_strength(self, value):
        self.combat_strength = value

    @property
    def get_health_points(self):
        return self.health_points

    @get_health_points.setter
    def set_health_points(self, value):
        self.health_points = value

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")

    def monster_attacks(self, hero):
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("The hero is dead")
        else:
            hero.health_points -= self.combat_strength
            print("The hero's health was reduced to: ", hero.health_points)


monster = Monster()
