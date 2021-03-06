# The gorilla class will repersent the state of a gorilla sprite that is controller by a player
# Ideally the x_pos and y_pos are float variables that reside on the top center of a Building rectangle
# player_id will link the gorilla class to the actual player.
# This class should provide the state information that allows the front end to render a gorilla that has
# its left arm up, right arm up, or both arms down at some position.
from Backend.Data.Enumerators import ArmState, GorillaLocation
import pygame

WIDTH = 50
HEIGHT = 50


class Gorilla:

    def __init__(self, x_pos: float, y_pos: float, player_id: str, location: GorillaLocation, width=WIDTH,
                 height=HEIGHT, ):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._player_id = player_id
        self._location = location
        self._arm_state = ArmState.ARM_DOWN
        self._arm_state_clock = 0

    def copy(self):
        g = Gorilla(self.x_pos, self.y_pos, self.player_id, self.location)
        g.__dict__.update(self.__dict__)
        return g

    def get_pos(self):
        return self._x_pos, self._y_pos

    def get_throw_start_pos(self):
        return self._x_pos, self._y_pos - self._height

    def get_size(self):
        return self._width, self._height

    @property
    def location(self):
        return self._location

    def __str__(self):
        arm_state_map = {
            ArmState.ARM_DOWN: "Arms Down",
            ArmState.LEFT_ARM_UP: "Left Arm Up",
            ArmState.RIGHT_ARM_UP: "Right Arm Up",
            ArmState.BOTH_ARM_UP: "Both Arms Up"
        }

        location_map = {
            GorillaLocation.RIGHT: "Right ",
            GorillaLocation.LEFT: "Left ",
        }
        out = [
            f"Position: ({self.x_pos}, {self.y_pos})",
            f"Size: ({self._width}, {self._height})"
            f"Player ID: {self.player_id}",
            f"Arms: {arm_state_map[self._arm_state]}",
            f"Location: {location_map[self._location]}",
            f"clock {self.arm_state_clock}"
        ]

        return ','.join(out)

    @property
    def arm_state_clock(self):
        return self._arm_state_clock

    @arm_state_clock.setter
    def arm_state_clock(self, clock):
        self._arm_state_clock = clock

    def decrement_clock(self):
        if self.arm_state_clock > 0:
            self._arm_state_clock = self._arm_state_clock - 1

    def get_pos(self):
        return self.x_pos, self.y_pos

    @property
    def x_pos(self) -> float:
        return self._x_pos

    @x_pos.setter
    def x_pos(self, value: float):
        self._x_pos = value

    @property
    def y_pos(self) -> float:
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: float):
        self._y_pos = value

    @property
    def player_id(self) -> str:
        return self._player_id

    @property
    def arm_state(self) -> int:
        return self._arm_state

    @arm_state.setter
    def arm_state(self, value: int):
        # TODO enforce that value is an enum and change type hints to use enum
        self._arm_state = value

    @property
    def rect(self):
        return pygame.Rect(self._x_pos, self._y_pos, self._width, self._height)
