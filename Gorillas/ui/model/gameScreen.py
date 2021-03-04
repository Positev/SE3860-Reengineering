import pygame

from ui.model.elements.sprites.windArrow import WindArrow
from ui.model.model import Model
from color import Color
from ui.model.elements.sprites.sun import Sun
from ui.model.elements.sprites.gorilla import Gorilla
from Backend.Controllers.GameController import GameController
from ui.model.elements.sprites.building import Building


class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE

    def __init__(self, screen_size, player_1_id, player_2_id):
        super(GameScreenModel, self).__init__(self.BACKGROUND_COLOR)
        self.render.append(pygame.sprite.Group())  # Building Layer
        self.render.append(pygame.sprite.Group())  # Main Layer
        self.render.append(pygame.sprite.Group())  # UI Layer

        # coordinate_adapter = CoordinateAdapter()
        self.game_controller = GameController(player_1_id, player_2_id, screen_size)
        game_state = self.game_controller.next_frame()
        # game_state = coordinate_adapter.adapt(self.game_controller.next_frame())

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
            building_pos = (building.x_pos, screen_size[1] - building.height)
            building_size = (building.width, building.height)
            new_building = Building(building.color, building_pos, building_size)
            self.render[0].add(new_building)
            self.buildings.append(new_building)
        # Create player one's gorilla
        self.gorilla_one = self.create_gorilla(game_state.gorillas[0], game_state.building[0])
        self.render[1].add(self.gorilla_one)
        # Create player two's gorilla
        self.gorilla_two = self.create_gorilla(game_state.gorillas[1], game_state.building[0])
        self.render[1].add(self.gorilla_two)
        """Implement the Input UI and Score UI when Adam has them ready
            Here's more space 
        """
        # Create the wind arrow
        self.wind_arrow = WindArrow(game_state.wind.direction, game_state.wind.velocity, screen_size)
        self.render[2].add(self.wind_arrow)
        # Create a list to store destruction in
        collision_list = ()
        collision_num = 0
        # Blit the objects to the background
        self.background.blit(self.sun.image, self.sun.rect)
        for building in self.buildings:
            self.background.blit(building.image, building.rect)
        self.background.blit(self.gorilla_one.image, self.gorilla_one.rect)
        self.background.blit(self.gorilla_two.image, self.gorilla_two.rect)
        """Space to add other UI elements in later when Adam is ready"""
        self.background.blit(self.wind_arrow.image, self.wind_arrow.rect)
        pygame.display.update()

    def create_gorilla(self, gorilla, building):
        """Creates a UI Gorilla object from given data"""
        pos = (gorilla.x_pos, gorilla.y_pos)
        size = (building.width * 5) / 8
        dimensions = (size, size)
        new_gorilla = Gorilla(dimensions, pos)
        return new_gorilla

    def update_frame(self, frame):
        """Updates the background to be a new frame of the game"""

