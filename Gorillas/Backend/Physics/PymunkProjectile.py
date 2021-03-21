# An extension of the projectile class to provide extra data for pymunk
import math
from math import cos, sin

import pymunk

from Backend.Data.Enumerators import ProjectileTravelDirection
from Backend.Data.Gorilla import WIDTH, HEIGHT
from Backend.Data.Projectile import Projectile


class PymunkProjectile(Projectile):
    COLLISION_TYPE = 0
    MASS = 5

    def __init__(self, initial_velocity: float,
                 launch_angle: float,
                 start_x: float,
                 start_y: float,
                 sender_id: str,
                 sprite: int,
                 direction: ProjectileTravelDirection,
                 key: int = 0,
                 width=WIDTH,
                 height=HEIGHT):
        Projectile.__init__(self, initial_velocity,
                            launch_angle,
                            start_x,
                            start_y,
                            sender_id,
                            sprite,
                            direction,
                            key,
                            width,
                            height)

        # https://github.com/viblo/pymunk/blob/master/examples/using_sprites.py
        vs = [(-23, 26), (23, 26), (0, -26)]
        moment = pymunk.moment_for_poly(self.MASS, vs)
        self.body = pymunk.Body(self.MASS, moment)
        self.shape = pymunk.Poly(self.body, vs)
        self.body.position = (start_x, start_y)
        self.body.angle = self.rotation
        self.body.velocity = self.initial_velocity * cos(math.radians(launch_angle )), self.initial_velocity * sin(math.radians(launch_angle))
        self.shape.collision_type = self.COLLISION_TYPE

    def get_pos(self):
        return self.body.position.x, self.body.position.y

    def add_to_space(self, space):
        space.add(self.body, self.shape)
