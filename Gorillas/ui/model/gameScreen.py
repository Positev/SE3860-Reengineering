import pygame

from Backend.Data.WorldDestruction import WorldDestruction
from ui.model.elements.sprites.banana import Banana
from ui.model.elements.sprites.collisions import Collisions
from ui.model.elements.sprites.windArrow import WindArrow
from ui.model.model import Model
from color import Color
from ui.model.elements.sprites.sun import Sun
from ui.model.elements.sprites.gorilla import Gorilla
from Backend.Controllers.GameController import GameController
from ui.model.elements.sprites.building import Building
from Backend.Adapters.CoordinateAdapter import CoordinateAdapter


class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE
    GORILLA_IMAGE = pygame.image.load("Sprites/Doug/doug.png")
    GORILLA_LEFT = pygame.image.load("Sprites/Doug/dougLeft.png")
    GORILLA_RIGHT = pygame.image.load("Sprites/Doug/dougRight.png")

    def __init__(self, screen_size, player_1_id, player_2_id):
        super(GameScreenModel, self).__init__(self.BACKGROUND_COLOR)
        self.render.append(pygame.sprite.Group())  # Building Layer
        self.render.append(pygame.sprite.Group())  # Main Layer
        self.render.append(pygame.sprite.Group())  # UI Layer

        coordinate_adapter = CoordinateAdapter(screen_size)
        self.game_controller = GameController(player_1_id, player_2_id, screen_size)
        game_state = coordinate_adapter.adapt(self.game_controller.next_frame())

        # Create the background
        self.background = pygame.Surface(screen_size)
        self.background = self.background.convert()
        self.background.fill(self.BACKGROUND_COLOR)
        # Create the Sun object. Won't move.
        sun_width = screen_size[0] / 20
        sun_height = screen_size[1] / 30
        sun_x_pos = (screen_size[0] - sun_width) / 2
        sun_y_pos = (screen_size[1] - sun_height) / 10
        self.sun = Sun(sun_width, sun_height, sun_x_pos, sun_y_pos)
        self.render[1].add(self.sun)
        # Create the buildings
        self.buildings = []
        for building in game_state.building:
            building_pos = (building.x_pos, building.y_pos - building.height)
            building_size = (building.width, building.height)
            new_building = Building(building.color, building_pos, building_size)
            self.render[0].add(new_building)
            self.buildings.append(new_building)
        # Create player one's gorilla
        self.gorilla_one = self.create_gorilla(game_state.gorillas[0], game_state.building[0], self.GORILLA_IMAGE)
        self.render[1].add(self.gorilla_one)
        # Create player two's gorilla
        self.gorilla_two = self.create_gorilla(game_state.gorillas[1], game_state.building[0], self.GORILLA_IMAGE)
        self.render[1].add(self.gorilla_two)
        """Implement the Input UI and Score UI when Adam has them ready
            Here's more space 
        """
        # Create the wind arrow
        self.wind_arrow = WindArrow(game_state.wind.direction, game_state.wind.velocity, screen_size)
        self.render[2].add(self.wind_arrow)
        # Create a list to store destruction in
        self.collision_list = ()
        self.collision_num = 0
        # Create a projectile placeholder to use when updating the scene
        # May need to update in later revisions if there are multiple projectiles
        self.projectile = Banana((30, 20), (0, 0))
        self.projectile.transparent()
        self.render[1].add(self.projectile)
        # Blit the objects to the background
        self.background.blit(self.sun.image, self.sun.rect)
        for building in self.buildings:
            self.background.blit(building.image, building.rect)
        self.background.blit(self.gorilla_one.image, self.gorilla_one.rect)
        self.background.blit(self.gorilla_two.image, self.gorilla_two.rect)
        """Space to add other UI elements in later when Adam is ready"""
        self.background.blit(self.wind_arrow.image, self.wind_arrow.rect)
        self.background.blit(self.projectile.image, self.projectile.rect)
        pygame.display.update()

    def create_gorilla(self, gorilla, building, image):
        """Creates a UI Gorilla object from given data"""
        size = gorilla.get_size()
        pos = (gorilla.x_pos - size[0] / 2, gorilla.y_pos - size[1])
        new_gorilla = Gorilla(size, pos, image)
        return new_gorilla

    def update_frame(self, frame):
        """Updates the background to be a new frame of the game"""
        # Update the gorillas
        if frame.gorillas[0].arm_state == frame.gorillas[0].arm_state.ARM_DOWN:
            self.gorilla_one.image = self.GORILLA_IMAGE
        elif frame.gorillas[0].arm_state == frame.gorillas[0].arm_state.LEFT_ARM_UP:
            self.gorilla_one.image = self.GORILLA_LEFT
        elif frame.gorillas[0].arm_state == frame.gorillas[0].arm_state.RIGHT_ARM_UP:
            self.gorilla_one.image = self.GORILLA_RIGHT

        if frame.gorillas[1].arm_state == frame.gorillas[1].arm_state.ARM_DOWN:
            self.gorilla_two.image = self.GORILLA_IMAGE
        elif frame.gorillas[1].arm_state == frame.gorillas[1].arm_state.LEFT_ARM_UP:
            self.gorilla_two.image = self.GORILLA_LEFT
        elif frame.gorillas[1].arm_state == frame.gorillas[1].arm_state.RIGHT_ARM_UP:
            self.gorilla_two.image = self.GORILLA_RIGHT

        # Update the projectile
        if frame.turn_active():
            projectile_pos = (frame.active_projectiles[0].current_x, frame.active_projectiles[0].current_y)
            self.projectile.rect = pygame.Rect(projectile_pos[0], projectile_pos[1], self.projectile.size[0], self.projectile.size[1])
            self.projectile.visible()
        else:
            self.projectile.transparent()

        # Create collisions if a new collision has appeared
        if self.collision_num < len(frame.destruction):
            new_collision = Collisions(frame.destruction[self.collision_num])
            self.collision_list.add(new_collision)
            self.render[1].add(new_collision)
            self.background.blit(self.collision_list[self.collision_num].image, self.sollision_list[self.collision_num].rect)
            self.collision_num = self.collision_num + 1
            self.projectile.transparent()

        # Update the wind
        new_width = frame.wind.velocity * self.wind_arrow.WIND_DEFAULT_WIDTH
        self.wind_arrow.image = pygame.transform.scale(self.wind_arrow.image, (new_width, self.wind_arrow.WIND_HEIGHT))
        if self.wind_arrow.direction != frame.wind.direction:
            self.wind_arrow.image = pygame.transform.flip(self.wind_arrow.image, True, False)
        self.wind_arrow.rect = pygame.Rect(self.wind_arrow.wind_pos[0], self.wind_arrow.wind_pos[1], new_width, self.wind_arrow.WIND_HEIGHT)

        """Room to update UI Elements when working on combining all branches into a coherent branch"""

        # Update the background
        pygame.display.update()
