from typing import Tuple, List

from Backend.Adapters.CoordinateAdapter import CoordinateAdapter
from Backend.Controllers.BuildingGenerator import BuildingGenerator
from Backend.Controllers.GorillaController import GorillaController
from Backend.Controllers.ProjectileHandler import ProjectileHandler
from Backend.Data.Enumerators import GorillaLocation
from Backend.Data.GameState import GameState
from Backend.Data.Gorilla import Gorilla
from Backend.Data.ScoreKeeper import ScoreKeeper
from Backend.Data.Wind import Wind


class GameController:

    def __init__(self, player_1_id, player_2_id, screen_size: Tuple[int,int], ):
        building_generator = BuildingGenerator()
        buildings = building_generator.generate_buildings(screen_size)

        player_1_pos = buildings[1].top_center()
        player_1 = Gorilla(player_1_pos[0],player_1_pos[1], player_1_id, GorillaLocation.LEFT)


        player_2_pos = buildings[-2].top_center()
        player_2 = Gorilla(player_2_pos[0],player_2_pos[1], player_2_id, GorillaLocation.RIGHT)

        score_keeper = ScoreKeeper()
        wind = Wind(velocity=1)
        turn_active = False

        self._game_state = GameState(
            buildings,
            [player_1,player_2],
            [],
            [],
            score_keeper,
            wind,
            turn_active
        )

    def throw_projectile(self, angle: float, velocity: float):
        projectile = ProjectileHandler(self.game_state.wind).launch_projectile(
            velocity,
            angle,
            self._game_state.active_player().get_pos(),
            0,
            self._game_state.active_player().player_id
        )
        self._game_state.active_projectiles.append(projectile)

        gorilla_controller = GorillaController(self._game_state.active_player())
        gorilla_controller.throw()

    def next_frame(self):
        #TODO return copy of game state
        updated_projectiles = ProjectileHandler(self._game_state.wind).move_projectiles(self._game_state.active_projectiles)
        self._game_state.active_projectiles = updated_projectiles

        for player in self._game_state.gorillas:
            controller = GorillaController(player)
            controller.handle_new_frame()

        return self._game_state.copy()


    
    @property
    def game_state(self) -> float:
        #TODO return copy of game state
        return self._game_state.copy()


if __name__ == '__main__':
    screen_size = (400,600)
    controller = GameController("player_1", "player_2", screen_size)
    coordinate_adapter = CoordinateAdapter(screen_size)
    controller.throw_projectile(30, 5, )
    print(controller.game_state)
    for i in range (1):
        frame = controller.next_frame()
        print(frame)
        print(coordinate_adapter.adapt(frame))

