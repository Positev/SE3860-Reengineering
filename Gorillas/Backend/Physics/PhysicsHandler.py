from typing import Tuple

import pymunk, time
from pymunk import Vec2d


# Physics handler will take respobsibility of creating and moving projecitles
# To progress animation, call next_time_step then get the active projectiles
from Backend.Controllers.GameController import GameController
from Backend.Data.Enumerators import ProjectileTravelDirection
from Backend.Physics.PymunkBuilding import PymunkBuilding
from Backend.Physics.PymunkProjectile import PymunkProjectile


class PhysicsHandler:

    CREATED_PROJECTILES = 0

    def __init__(self, buildings, gorillas):
        self.buildings = buildings
        self.gorillas = gorillas

        self.active_projectiles = []
        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0.0, -90.0)

        for gorilla in self.gorillas:
            gorilla.add_to_space(self.space)

        for building in self.buildings:
            building.add_to_space(self.space)
        self.handler = self.space.add_collision_handler(PymunkProjectile.COLLISION_TYPE, PymunkBuilding.COLLISION_TYPE)
        self.handler.begin = self.remove_first

    def remove_first(self, arbiter, space, data):
        ball_shape = arbiter.shapes[0]

        collided_projectiles = []
        collided_buildings = []
        collided_world_destructions = []
        collided_gorillas = []

        for shape in arbiter.shapes:
            for gorilla in self.gorillas:
                pass
            for building in self.buildings:
                pass
            for projectile in self.active_projectiles:
                pass
            for destruction in self.world_destruction:
                pass

        for shape in arbiter.shapes:


        space.remove(ball_shape, ball_shape.body)
        return True

    # This will add a new projectile to the scene
    # and generate a pymunk projectile object
    # to be managed locally
    def throw_projectile(self, velocity: float, angle: float,  start_pos: Tuple[float, float], sprite: int,
                         sender_id: str, travel_direction: ProjectileTravelDirection):

        new_projectile = PymunkProjectile(velocity, angle, start_pos[0], start_pos[1], sender_id, sprite,travel_direction, key=self.CREATED_PROJECTILES)
        self.CREATED_PROJECTILES += 1
        self.active_projectiles.append(new_projectile)
        new_projectile.add_to_space(self.space)
        return new_projectile


    # compute next step in physics
    def next_time_step(self, dt = 1/60):
        self.space.step(dt)


if __name__ == '__main__':
    gc = GameController("1","2", (400,400))
    print(gc.game_state)
    ph = PhysicsHandler(gc.game_state.building,gc.game_state.gorillas)
    ph.throw_projectile(30, 30, (30, 450), 0, "str", ProjectileTravelDirection.LEFT)

    while True:
        ph.next_time_step()
        time.sleep(.05)
        print(ph.active_projectiles[0].get_pos())


