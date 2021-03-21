# An extension of the projectile class to provide extra data for pymunk
import pymunk

from Gorillas.Backend.Data.Enumerators import ProjectileTravelDirection
from Gorillas.Backend.Data.Projectile import Projectile, WIDTH, HEIGHT


class PymunkProjectile(Projectile):

    COLLISION_TYPE = 'projectile'
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


        #https://github.com/viblo/pymunk/blob/master/examples/using_sprites.py
        vs = [(-23, 26), (23, 26), (0, -26)]
        moment = pymunk.moment_for_poly(self.MASS, vs)
        self.body = pymunk.Body(self.MASS, moment)
        self.shape = pymunk.Poly(self.body, vs)
        self.body.position = self.get_pos()
        self.body.angle = self.rotation
        self.shape.collision_type = self.COLLISION_TYPE

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

    def add_to_space(self, space):
        space.add(self.body, self.shape)
