import pymunk

from Backend.Data.WorldDestruction import WorldDestruction


class PymunkDestruction(WorldDestruction):

    def __init__(self, center_x, center_y, radius, *args):
        self.body = pymunk.Body(1, 1, body_type=pymunk.Body.STATIC)
        self.shape = pymunk.shapes.Circle(self.body, radius)

        self.shape.filter = pymunk.ShapeFilter(categories=2)
        self._radius = radius
        WorldDestruction.__init__(self, center_x, center_y, radius, radius, radius, radius)

    def radius(self):
        return self._radius

    def add_to_space(self, space):
        space.add(self.body, self.shape)
