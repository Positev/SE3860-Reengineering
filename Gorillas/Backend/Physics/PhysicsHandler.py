from typing import Tuple

import pymunk
from pymunk import Vec2d


# Physics handler will take respobsibility of creating and moving projecitles
# To progress animation, call next_time_step then get the active projectiles
from Backend.Data.Enumerators import ProjectileTravelDirection
from Backend.Physics.PymunkProjectile import PymunkProjectile


class PhysicsHandler:

    CREATED_PROJECTILES = 0

    def __init__(self, buildings, gorillas):
        self.buildings = buildings
        self.gorillas = gorillas
        self.active_projectiles = []
        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0.0, -9.0)

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
    ph = PhysicsHandler([],[])
    ph.throw_projectile(30, 30, (0, 0), 0, "str", ProjectileTravelDirection.LEFT)
    while True:
        ph.next_time_step()
        print(ph.active_projectiles[0])


