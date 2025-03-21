class Character():
    def __init__(self, combat_strength, health_points):
        self.__combat_strength = combat_strength
        self.__health_points = health_points

    @property
    def get_combat_strength(self):
        return self.__combat_strength

    @get_combat_strength.setter
    def set_combat_strength(self, value):
        self.__combat_strength = value

    @property
    def get_health_points(self):
        return self.__health_points

    @get_health_points.setter
    def set_health_points(self, value):
        self.__health_points = value

    def