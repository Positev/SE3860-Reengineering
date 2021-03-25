from Backend.Data.Enumerators import CollisionResult


class Collision:
    def __init__(self, x_pos: float, y_pos: float, collision_result: CollisionResult, projectile_id, collided_id = 0):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__collision_result = collision_result
        self._projectile_id = projectile_id
        if collision_result != CollisionResult.OUT_OF_BOUNDS:
            self._collided_id = collided_id

    def __str__(self):
        result_map = {
            CollisionResult.NO_HIT: "NO HIT",
            CollisionResult.BUILDING_HIT: "BUILDING HIT",
            CollisionResult.PLAYER_HIT: "PLAYER HIT",
            CollisionResult.OUT_OF_BOUNDS: "OUT OF BOUNDS"
        }
        out = [
            f"x: {self.__x_pos}",
            f"y: {self.__y_pos}",
            f"result: {result_map[self.__collision_result]}",
            f"projectile ID: {self._projectile_id}",
            f"collidedID: {self._collided_id}" if self.collision_result != CollisionResult.OUT_OF_BOUNDS else ""
        ]
        return ', '.join(out)

    def projectile_id(self):
        return self._projectile_id

    def collided_id(self):
        return self._collided_id

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
