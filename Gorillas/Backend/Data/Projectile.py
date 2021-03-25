import pygame

from Backend.Data.Enumerators import ProjectileTravelDirection

WIDTH = 30
HEIGHT = 20

class Projectile:
    def __init__(self, 
                 initial_velocity: float, 
                 launch_angle: float, 
                 start_x:float, 
                 start_y: float,
                 sender_id: str, 
                 sprite: int,
                 direction: ProjectileTravelDirection,
                 key: int = 0,
                 width = WIDTH,
                 height = HEIGHT):

        self._initial_velocity = initial_velocity
        self._launch_angle = launch_angle
        self._start_x = start_x
        self._start_y = start_y
        self._width = width
        self._height = height
        self._direction = direction
        self._rotation = 0
        self._flight_time = 0
        self._current_x = 0
        self._current_y = 0
        self._key = key
        self._sender_id = sender_id
        self._sprite = sprite



    def __str__(self):
        out = [
            f"Key: {self._key}",
            f"Initial Velocity: {self.initial_velocity}",
            f"Launch Angle: {self.launch_angle}",
            f"Flight Time: {self.flight_time}",
            f"Start Position: ({self.start_x},{self.start_y})",
            f"Size: ({self._width}, {self._height})",
            f"Rotation: {self._rotation}",
            f"Current Position: {self.get_pos()}",
            f"Sender ID: {self.sender_id}",
            f"Sprite:  {self.sprite}",

        ]

        return ','.join(out)

    def copy(self):
        p = Projectile(self.initial_velocity, self.launch_angle, self.start_x, self.start_y, self.sender_id, self.sprite, self._direction)
        p.__dict__.update(self.__dict__)
        return p

    def get_pos(self):
        return self.current_x, self.current_y

    def get_size(self):
        return self._width, self._height

    def direction(self):
        return self._direction

    @property
    def initial_velocity(self) -> float:
        return self._initial_velocity

    def key(self) -> int:
        return self._key

    @initial_velocity.setter
    def initial_velocity(self, value: float):
        self._initial_velocity = value

    @property
    def launch_angle(self) -> float:
        return self._launch_angle

    @launch_angle.setter
    def launch_angle(self, value: float):
        self._launch_angle = value

    @property
    def rotation(self) -> float:
        return self._rotation

    @rotation.setter
    def rotation(self, value: float):
        self._rotation = value


    @property
    def start_x(self) -> float:
        return self._start_x

    @start_x.setter
    def start_x(self, value: float):
        self._start_x = value

    @property
    def start_y(self) -> float:
        return self._start_y

    @start_y.setter
    def start_y(self, value: float):
        self._start_y = value



    @property
    def current_x(self) -> float:
        return self._current_x

    @current_x.setter
    def current_x(self, value: float):
        self._current_x = value

    @property
    def current_y(self) -> float:
        return self._current_y

    @current_y.setter
    def current_y(self, value: float):
        self._current_y = value


    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value





    @property
    def sender_id(self) -> str:
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value: str):
        self._sender_id = value

    @property
    def flight_time(self) -> str:
        return self._flight_time

    
    def increment_flight_time(self):
        #TODO Probably can tune this value.
        self._flight_time += .2

    @property
    def sprite(self) -> int:
        return self._sprite

    @sprite.setter
    def sprite(self, value: int):
        #TODO Enforce that sprite is instance of enum
        self._sprite = value

    @property
    def rect(self):
        return pygame.Rect(*self.get_pos(), *self.get_size())