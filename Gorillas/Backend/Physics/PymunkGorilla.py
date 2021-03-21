# An extension of the Gorilla class to provide extra data for pymunk
import pymunk

from Gorillas.Backend.Data.Enumerators import GorillaLocation
from Gorillas.Backend.Data.Gorilla import Gorilla, HEIGHT, WIDTH


class PymunkGorilla(Gorilla):
    COLLISION_TYPE = 2
    MASS = 10

    def __init__(self, x_pos: float, y_pos: float, player_id: str, location: GorillaLocation, width=WIDTH,
                 height=HEIGHT):
        half_w = width / 2
        half_h = height

        center = x_pos, y_pos + half_h

        vs = [(half_w, half_h), (-half_w, half_h), (half_w, -half_h), (-half_w, -half_h)]

        moment = pymunk.moment_for_poly(self.MASS, vs)

        self.body = pymunk.Body(self.MASS, moment)
        self.shape = pymunk.Poly(self.body, vs)
        self.body.position = center
        self.shape.collision_type = self.COLLISION_TYPE

        Gorilla.__init__(self, x_pos, y_pos, player_id, location, width=width, height=height)

    def add_to_space(self, space):
        space.add(self.body, self.shape)
