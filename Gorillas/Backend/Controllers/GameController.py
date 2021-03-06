from typing import Tuple, List

from Backend.Adapters.CoordinateAdapter import CoordinateAdapter
from Backend.Controllers.BuildingGenerator import BuildingGenerator
from Backend.Controllers.CollisionHandler import CollisionHandler
from Backend.Controllers.GorillaController import GorillaController
from Backend.Controllers.ProjectileHandler import ProjectileHandler
from Backend.Data.Enumerators import GorillaLocation, ProjectileTravelDirection
from Backend.Data.GameState import GameState
from Backend.Data.Gorilla import Gorilla
from Backend.Data.ScoreKeeper import ScoreKeeper
from Backend.Data.Wind import Wind
from Backend.Data.WorldDestruction import WorldDestruction


class GameController:

    # TODO add gravity parameter
    def __init__(self, player_1_id, player_2_id, screen_size: Tuple[int, int], gravity: float = 1):
        building_generator = BuildingGenerator()
        buildings = building_generator.generate_buildings(screen_size)
        self._screen_size = screen_size
        ProjectileHandler.GRAVITY = gravity

        player_1_pos = buildings[1].top_center()
        player_1 = Gorilla(player_1_pos[0], player_1_pos[1], player_1_id, GorillaLocation.LEFT)

        player_2_pos = buildings[-2].top_center()
        player_2 = Gorilla(player_2_pos[0], player_2_pos[1], player_2_id, GorillaLocation.RIGHT)

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

    def throw_projectile(self, angle: float, velocity: float):
        player = self._game_state.active_player()
        projectile = ProjectileHandler(self.game_state.wind).launch_projectile(
            velocity,
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
            if projectile.key() == collision.projectile_id():
                print(f"\tprojectile -> {projectile}")
                projectileForCollision = projectile
        for collider in self._game_state.building:
            if collider.key() == collision.collided_id():
                self._game_state.destruction.append(WorldDestruction(collision.x_pos, collision.y_pos, 30, 0, 0, 15))
                print(f"\tCollided With -> {collider}")
        for player in self._game_state.gorillas:
            if player.player_id == collision.collided_id():
                self._game_state.destruction.append(WorldDestruction(collision.x_pos, collision.y_pos, 45, 0, 0, 15))
                self._game_state.score.record_win(projectileForCollision.sender_id)
                print(f"\t{player.player_id} has been hit!")

        projectiles.remove(projectileForCollision)

    def next_frame(self):

        projectile_handler = ProjectileHandler(self._game_state.wind)
        updated_projectiles = projectile_handler.move_projectiles(self._game_state.active_projectiles)
        collisions = CollisionHandler.test_collisions(
            updated_projectiles,
            self._game_state.building,
            self._game_state.gorillas, self._screen_size
        )


        #for p in updated_projectiles:
        #    print(p.get_pos())
        if len(collisions) > 0:
            for collision in collisions:
                self._handle_collision(collision, updated_projectiles)

            self._game_state.next_player()
            self._game_state.turn_active = False
        elif any([projectile_handler.projectile_out_of_screen(proj, self._screen_size) for proj in updated_projectiles]):
            for proj in updated_projectiles:
                if projectile_handler.projectile_out_of_screen(proj, self._screen_size):
                    print("Projectile out of screen")
                    updated_projectiles.remove(proj)
            self._game_state.next_player()
            self._game_state.turn_active = False

            # TODO handle colliion result
            #   Remove active projectile
            #   add world destruction
            #   trigger game over if player hit

            # TODO Handle turn change when projectile is removed

        self._game_state.active_projectiles = updated_projectiles

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


