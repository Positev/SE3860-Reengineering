from typing import Tuple, List
import math

from Backend.Data.Enumerators import ProjectileTravelDirection
from Backend.Data.Projectile import Projectile

PATH_STEP_PER_FRAME = 0.1



# TODO Docs
# TODO Write tests for this
class ProjectileHandler:

    CREATED_PROJECTILES = 0
    GRAVITY = .001

    def __init__(self, wind):
        # TODO implement when all sub-controllers are ready
        self._game_state = {}
        self.wind = wind

    def _compute_next_position(self, projectile):
        projectile.increment_flight_time()
        projectile_direction = -1 if projectile.direction() == ProjectileTravelDirection.LEFT else 1
        # TODO convert to use wind object when implemented
        wind_velocity = 1

        # y = y_0 + V_0_y * t + (g/2)*t^2
        # x += (PATH_STEP_PER_FRAME - wind_velocity) * t
        cosine = math.cos(math.radians(projectile.launch_angle))
        sine = math.sin(math.radians(projectile.launch_angle))

        vx = projectile.initial_velocity * cosine
        vy = projectile.initial_velocity * sine

        new_x = projectile_direction * vx * projectile.flight_time + wind_velocity + projectile.start_x
        new_y = vy * projectile.flight_time - (self.GRAVITY / 2) * (projectile.flight_time ** 2) + projectile.start_y

        projectile.current_x = new_x
        projectile.current_y = new_y
        return projectile

    def projectile_out_of_screen(self, projectile, screen_size):
        cur_x, cur_y = projectile.get_pos()
        w,h = screen_size
        return cur_x < 0 or cur_x > w or 0 > cur_y

    # This function will step through each projectile and update thier position
    def move_projectiles(self, projectiles: List[Projectile]) -> List[Projectile]:
        new_projectiles = []

        for projectile in projectiles:
            updated_projectile = self._compute_next_position(projectile)
            new_projectiles.append(updated_projectile)

        return new_projectiles

    # This function just creates a new projectile and adds it to the list of projectiles
    def launch_projectile(self, velocity: float, angle: float,  start_pos: Tuple[float, float], sprite: int,
                          sender_id: str, travel_direction: ProjectileTravelDirection) -> Projectile:

        new_projectile = Projectile(velocity, angle, start_pos[0], start_pos[1], sender_id, sprite,travel_direction, key=self.CREATED_PROJECTILES)
        self.CREATED_PROJECTILES += 1
        return new_projectile
