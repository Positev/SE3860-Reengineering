import math
from math import cos, sin
from typing import Tuple

import pymunk
import time
# Physics handler will take respobsibility of creating and moving projecitles
# To progress animation, call next_time_step then get the active projectiles
from Backend.Controllers.GameController import GameController
from Backend.Data.Collision import Collision
from Backend.Data.Enumerators import ProjectileTravelDirection, CollisionResult, WindDirection
from Backend.Physics.PymunkBuilding import PymunkBuilding
from Backend.Physics.PymunkDestruction import PymunkDestruction
from Backend.Physics.PymunkGorilla import PymunkGorilla
from Backend.Physics.PymunkProjectile import PymunkProjectile
from pymunk import Vec2d


class PhysicsHandler:
    CREATED_PROJECTILES = 0

    def __init__(self, buildings, gorillas, on_collision_callback, gravity, wind, screen_size):
        self.buildings = buildings
        self.gorillas = gorillas
        self.screen_size = screen_size
        self.active_projectiles = []
        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0.0, -gravity)
        self.destruction = []
        self.wind = wind
        self.collision_callback = on_collision_callback
        for gorilla in self.gorillas:
            gorilla.add_to_space(self.space)

        for building in self.buildings:
            building.add_to_space(self.space)
        self.handler = self.space.add_collision_handler(PymunkProjectile.COLLISION_TYPE, PymunkBuilding.COLLISION_TYPE)
        self.handler.pre_solve = self.handle_building_hit

        self.handler = self.space.add_collision_handler(PymunkProjectile.COLLISION_TYPE, PymunkGorilla.COLLISION_TYPE)
        self.handler.post_solve = self.handle_gorilla_hit

    def handle_building_hit(self, arbiter, space, data):
        ball_shape = arbiter.shapes[0]

        for projectile in self.active_projectiles:
            if projectile.c_id == ball_shape.body._id:

                center = projectile.get_pos()
                dest_center = center
                for destruction in self.destruction:
                    d_center = destruction.get_center()
                    diff = center[0] - d_center[0], center[1] - d_center[1]
                    r_diff = diff[0] ** 2 + diff[1] ** 2
                    if r_diff < destruction.radius() ** 2:
                        velocity = ball_shape.body.velocity
                        inv_mag = 1 / ((velocity[0] ** 2 + velocity[1] ** 2) ** .5)
                        dest_displacement = (2.5 * velocity[0] * inv_mag), 2.5 * velocity[1] * inv_mag
                        dest_center = center[0] + dest_displacement[0], center[1] + dest_displacement[1]

                        return False
                dest = PymunkDestruction(*dest_center, 15)
                self.destruction.append(dest)
                dest.add_to_space(self.space)
                self.active_projectiles.remove(projectile)
                self.collision_callback(
                    Collision(*center, CollisionResult.BUILDING_HIT, projectile.c_id, arbiter.shapes[1].body._id, ),
                    [projectile])

        space.remove(ball_shape, ball_shape.body)
        return True

    def handle_gorilla_hit(self, arbiter, space, data):
        ball_shape = arbiter.shapes[0]

        for projectile in self.active_projectiles:
            if projectile.c_id == ball_shape.body._id:
                center = projectile.get_pos()
                self.active_projectiles.remove(projectile)
                self.collision_callback(
                    Collision(*center, CollisionResult.PLAYER_HIT, projectile.c_id, arbiter.shapes[1].body._id),
                    [projectile])

        space.remove(ball_shape, ball_shape.body)
        return True

    # This will add a new projectile to the scene
    # and generate a pymunk projectile object
    # to be managed locally
    def throw_projectile(self, velocity: float, angle: float, start_pos: Tuple[float, float], sprite: int,
                         sender_id: str, travel_direction: ProjectileTravelDirection):

        wind_diff = self.wind.velocity * (-1 if self.wind.direction == WindDirection.RIGHT else 1)

        velocity = velocity * cos(math.radians(angle)), velocity * sin(math.radians(angle))

        if travel_direction == ProjectileTravelDirection.LEFT:
            velocity = -velocity[0] + wind_diff, velocity[1]
        else:
            velocity = velocity[0] + wind_diff, velocity[1]

        new_projectile = PymunkProjectile(velocity, angle, start_pos[0], start_pos[1], sender_id, sprite,
                                          travel_direction, key=self.CREATED_PROJECTILES)
        self.CREATED_PROJECTILES += 1
        # self.active_projectiles.append(new_projectile)
        new_projectile.add_to_space(self.space)
        return new_projectile

    # compute next step in physics
    def next_time_step(self, dt=1 / 60):
        self.space.step(dt)
        for projectile in self.active_projectiles:
            cur_x, cur_y = projectile.get_pos()
            w, h = self.screen_size
            if cur_x < 0 or cur_x > w:
                self.active_projectiles.remove(projectile)
                self.collision_callback(
                    Collision(*projectile.get_pos(), CollisionResult.OUT_OF_BOUNDS, projectile.c_id),
                    self.active_projectiles)


if __name__ == '__main__':
    screen_size = (400, 425)
    gc = GameController("1", "2", screen_size)
    print(gc.game_state)
    ph = PhysicsHandler(gc.game_state.building, gc.game_state.gorillas, lambda x: print(x), 90, screen_size)

    while True:
        ph.next_time_step()
        time.sleep(.005)
        if len(ph.active_projectiles) == 0:
            ph.throw_projectile(float(input("Velocity")), float(input("Angle")), (30, 400), 0, "str",
                                ProjectileTravelDirection.LEFT)
        # print(ph.active_projectiles[0].get_pos())
