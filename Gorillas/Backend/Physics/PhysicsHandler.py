
import pymunk
from pymunk import Vec2d


# Physics handler will take respobsibility of creating and moving projecitles
# To progress animation, call next_time_step then get the active projectiles
class PhysicsHandler:

    def __init__(self, buildings, gorillas):
        pass

    # This will add a new projectile to the scene
    # and generate a pymunk projectile object
    # to be managed locally
    def throw_projectile(self):
        pass

    # compute next step in physics
    def next_time_step(self):
        pass



