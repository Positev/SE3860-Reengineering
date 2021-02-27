from Backend.Data.Enumerators import WindDirection


class Wind:
    def __init__(self, direction=WindDirection.LEFT, velocity=0):
        if (isinstance(direction, WindDirection)):
            self.__direction = direction
        else:
            raise Exception("Wrong data type.")
        if (velocity >= 0):
            self.__velocity = velocity
        else:
            raise Exception("Velocity must be greater than or equal to zero.")

    def __str__(self):
        direction_map = {
            WindDirection.LEFT : "Left",
            WindDirection.RIGHT : "Right",

        }

        out = [
            f"Velocity: {self.velocity}",
            f"Direction: {direction_map[self.direction]}"
        ]

        return ','.join(out)

    @property
    def direction(self):
        return self.__direction

    @property
    def velocity(self):
        return self.__velocity

    @direction.setter
    def direction(self, direction):
        if (isinstance(direction, WindDirection)):
            self.__direction = direction
        else:
            raise Exception("Wrong data type.")

    @velocity.setter
    def velocity(self, velocity):
        if (velocity >= 0):
            self.__velocity = velocity
        else:
            raise Exception("Velocity must be greater than or equal to zero.")
