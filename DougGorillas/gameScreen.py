import pygame
from model import Model
from color import Color
from sun import Sun
from Backend.Controllers.GameController import GameController
from Backend.Data.GameState import GameState


class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE

    def __init__(self, screen_size):
        super(GameScreenModel, self).__init__(self.BACKGROUND_COLOR)
        game_controller = GameController()
        game_state = game_controller.next_frame()

        # Create the background
        background = pygame.surface(screen_size)
        background = background.convert()
        background.fill(self.BACKGROUND_COLOR)
        # Create the Sun object. Won't move.
        sun_width = screen_size[0] / 20
        sun_height = screen_size[1] / 30
        sun_x_pos = (screen_size[0] - sun_width) / 2
        sun_y_pos = (screen_size[1] - sun_height) / 10
        sun = Sun(sun_width, sun_height, sun_x_pos, sun_y_pos)

