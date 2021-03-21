# An extension of the Building class to provide extra data for pymunk
from typing import Tuple

import pymunk

from Backend.Data.Building import Building


class PymunkBuilding(Building):
    COLLISION_TYPE = 1
    MASS = 100

    def __init__(self, x_pos: float, y_pos: float, color: Tuple[int, int, int], width: float, height: float,
                 key: int = 0):
        half_w = width / 2
        half_h = height
        center = x_pos, y_pos

        vs = [ (-half_w, half_h),(half_w, half_h), (half_w, -half_h), (-half_w, -half_h)]

        moment = pymunk.moment_for_poly(self.MASS, vs)


        self.body = pymunk.Body(self.MASS, moment,  body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly(self.body, vs)
        self.body.position = center
        self.shape.collision_type = self.COLLISION_TYPE
        self.shape.filter = pymunk.ShapeFilter(categories=1)
        self.c_id = self.body._id
        Building.__init__(self, x_pos, y_pos, color, width,height, key, )

    def add_to_space(self, space):
        space.add(self.body, self.shape)
