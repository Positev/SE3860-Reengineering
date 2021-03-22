from typing import Tuple, List

from Backend.Adapters.CoordinateAdapter import CoordinateAdapter
from Backend.Controllers.BuildingGenerator import BuildingGenerator
from Backend.Controllers.CollisionHandler import CollisionHandler
from Backend.Controllers.GorillaController import GorillaController
from Backend.Controllers.ProjectileHandler import ProjectileHandler
from Backend.Data.Enumerators import GorillaLocation, ProjectileTravelDirection, CollisionResult
from Backend.Data.GameState import GameState
from Backend.Data.Gorilla import Gorilla
from Backend.Data.ScoreKeeper import ScoreKeeper
from Backend.Data.Wind import Wind
from Backend.Data.WorldDestruction import WorldDestruction
from Backend.Physics.PymunkGorilla import PymunkGorilla


class GameController:

    # TODO add gravity parameter
    def __init__(self, player_1_id, player_2_id, screen_size: Tuple[int, int], gravity: float = 1):
        building_generator = BuildingGenerator()
        buildings = building_generator.generate_buildings(screen_size)
        self._screen_size = screen_size
        ProjectileHandler.GRAVITY = gravity

        player_1_pos = buildings[1].top_center()
        player_1 = PymunkGorilla(player_1_pos[0], player_1_pos[1], player_1_id, GorillaLocation.LEFT)

        player_2_pos = buildings[-2].top_center()
        player_2 = PymunkGorilla(player_2_pos[0], player_2_pos[1], player_2_id, GorillaLocation.RIGHT)

        score_keeper = ScoreKeeper(player_1_id, player_2_id)
        wind = Wind(velocity=1)
        turn_active = False

        self._game_state = GameState(
            buildings,
            [player_1, player_2],
            [],
            [],
            score_keeper,
            wind,
            turn_active
        )

        from Backend.Physics.PhysicsHandler import PhysicsHandler
        self.physics_handler = PhysicsHandler(buildings, [player_1, player_2], self._handle_collision, 90, screen_size)



    def throw_projectile(self, angle: float, velocity: float):

        player = self._game_state.active_player()
        projectile = self.physics_handler.throw_projectile(velocity,
                                              angle,
                                              player.get_throw_start_pos(),
                                              0,
                                              player.player_id,
                                              ProjectileTravelDirection.LEFT if player.location == GorillaLocation.RIGHT else ProjectileTravelDirection.RIGHT
                                              )

        self._game_state.active_projectiles.append(projectile)
        self._game_state.turn_active = True

        gorilla_controller = GorillaController(self._game_state.active_player())
        gorilla_controller.throw()

    def _handle_collision(self, collision, projectiles):
        print("Collision Occured")
        print(f"\t{collision}")
        projectileForCollision = None
        for projectile in projectiles:
            if projectile.c_id == collision.projectile_id():
                print(f"\tprojectile -> {projectile}")
                projectileForCollision = projectile

        if collision.collision_result != CollisionResult.OUT_OF_BOUNDS:
            for collider in self._game_state.building:
                if collider.c_id == collision.collided_id():
                    self._game_state.destruction.append(WorldDestruction(collision.x_pos, collision.y_pos, 30, 0, 0, 15))
                    print(f"\tCollided With -> {collider}")
            for player in self._game_state.gorillas:
                if player.c_id == collision.collided_id():
                    self._game_state.destruction.append(WorldDestruction(collision.x_pos, collision.y_pos, 45, 0, 0, 15))
                    self._game_state.score.record_win(projectileForCollision.sender_id)
                    print(f"\t{player.player_id} has been hit!")

        if projectileForCollision in self._game_state.active_projectiles:
            self._game_state.active_projectiles.remove(projectileForCollision)


        self._game_state.next_player()
        self._game_state.turn_active = False

    def next_frame(self):

        self.physics_handler.next_time_step()


        self._game_state.active_projectiles = self.physics_handler.active_projectiles

        for player in self._game_state.gorillas:
            controller = GorillaController(player)
            controller.handle_new_frame()

        return self._game_state.copy()

    @property
    def game_state(self) -> float:
        # TODO return copy of game state
        return self._game_state.copy()


if __name__ == '__main__':
    screen_size = (400, 600)
    gravity = input("Enter Gravity: ")
    p1 = input("Enter a name for player 1: ")
    p2 = input("Enter a name for player 2: ")
    controller = GameController(p1, p2, screen_size)
    coordinate_adapter = CoordinateAdapter(screen_size)


    with open("buildings.txt", 'w+') as output:
        frame = controller.next_frame()
        for b in frame.building:
            output.write(b.graphable())
            output.write("\n")

    with open("p1.csv", 'w+') as output1:
        with open("p2.csv", 'w+') as output2:

            while True:

                frame = controller.next_frame()
                print(frame)
                print()
                for proj in frame.active_projectiles:
                    pos = proj.get_pos()
                    if proj.sender_id == "player_1":
                        output1.write(f"{pos[0]}, {pos[1]}" + "\n")
                    else:
                        output2.write(f"{pos[0]}, {pos[1]}" + "\n")

                if not frame.turn_active:
                    print(f"{frame.active_player().player_id}, throw your banana.")
                    velocity = float(input("Input a velocity: "))
                    launch_angle = float(input("Input a launch angle: "))
                    controller.throw_projectile(launch_angle, velocity)


