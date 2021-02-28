from Backend.Data.Enumerators import CollisionResult


class Collision:
    def __init__(self, x_pos: float, y_pos: float, collision_result: CollisionResult):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__collision_result = collision_result

    @property
    def x_pos(self):
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, x_pos):
        self.__x_pos = x_pos

    @property
    def y_pos(self):
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, y_pos):
        self.__y_pos = y_pos

    @property
    def collision_result(self):
        return self.__collision_result

    @collision_result.setter
    def collision_result(self, collision_result):
        self.__collision_result = collision_result
