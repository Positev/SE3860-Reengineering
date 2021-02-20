from typing import Tuple, List
from Gorillas.Backend.Data.Projectile import Projectile

PATH_STEP_PER_FRAME = 1

class ProjectileHandler:

    def __init__(self, ):
        #TODO implement when all sub-controllers are ready
        self._game_state = {}

    def move_projectiles(self, projectiles: List[Projectile]):
        #TODO Implement
        pass

    def launch_projectile(self, velocity: float, angle:float, start_pos:Tuple[float, float], sprite: int, sender_id: str):
        
        #TODO Implement
        pass
    
    @property
    def game_state(self) -> float:
        return self._game_state

  