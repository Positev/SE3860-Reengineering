import pygame
from ui.model.model import Model
from color import Color
from ui.model.elements.sprites.sun import Sun
from ui.model.elements.sprites.gorilla import Gorilla
from Backend.Controllers.GameController import GameController


class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE
    WIND_DEFAULT_WIDTH = 50
    WIND_HEIGHT = 30

    def __init__(self, screen_size, player_1_id, player_2_id):
        super(GameScreenModel, self).__init__(self.BACKGROUND_COLOR)
        self.game_controller = GameController(player_1_id, player_2_id, screen_size)
        game_state = self.game_controller.next_frame()

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
        # Create the buildings
        self.buildings = []
        for building in game_state.building:
            self.buildings.append(pygame.Rect(building.x_pos, screen_size[1] - building.height, building.width, building.height))
        # Create player one's gorilla
        self.gorilla_one = self.create_gorilla(game_state.gorillas[0], game_state.building[0])
        # Create player two's gorilla
        self.gorilla_two = self.create_gorilla(game_state.gorillas[1], game_state.building[0])
        """Implement the Input UI and Score UI when Adam has them ready
            Here's more space 
        """
        # Create the wind arrow
        self.arrow_image = pygame.image.load("Sprites/arrow.png")
        wind_width = game_state.wind.velocity * self.WIND_DEFAULT_WIDTH
        self.arrow_image = pygame.transform.scale(self.arrow_image, (wind_width, self.WIND_HEIGHT))
        self.wind_pos = ((screen_size[0] - wind_width) / 2, (screen_size[1] - self.WIND_HEIGHT))
        wind_rect = pygame.Rect(self.wind_pos[0], self.wind_pos[1], wind_width, self.WIND_HEIGHT)
        # Create a list to store destruction in
        collision_list = ()
        collision_num = 0
        # Blit the opjects to the background
        self.background.blit(self.sun.defaultImage, self.sun.rect)
        counter = 0
        for building in self.buildings:
            self.background.fill(game_state.building[counter].color, building, special_flags=0)
            counter = counter + 1
        self.background.blit(self.gorilla_one.defaultImage, self.gorilla_one.rect)
        self.background.blit(self.gorilla_two.defaultImage, self.gorilla_two.rect)
        """Space to add other UI elements in later when Adam is ready"""
        self.background.blit(self.arrow_image, wind_rect)


    def create_gorilla(self, gorilla, building):
        """Creates a UI Gorilla object from given data"""
        pos = (gorilla.x_pos, gorilla.y_pos)
        size = (building.width * 5) / 8
        dimensions = (size, size)
        new_gorilla = Gorilla(dimensions, pos)
        return new_gorilla

    def update_frame(self, frame):
        """Updates the background to be a new frame of the game"""

