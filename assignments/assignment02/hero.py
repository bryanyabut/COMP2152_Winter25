import random

class Hero():
    def __init__(character):
        character.combat_strength = random.randint(1, 10)
        character.health_points = random.randint(1, 10)
    
    def get_combat_strength(self):
        return self.combat_strength
    
    def set_combat_strength(self, value):
        self.combat_strength = value

    def get_health_points(self):
        return self.combat_strength

    def set_health_points(self, value):
        self.health_points = value

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
    
    def hero_attacks(self, monster):
        if self.combat_strength >= monster.healh_points:
            monster.health_points = 0
            print("The monster is killed")
        else:
            monster.health_points -= self.combat_strength
            print("The monster's health was reduced to: ", monster.health_points)

hero = Hero()
print("The combat strength of the Hero is: ", hero.get_combat_strength())
