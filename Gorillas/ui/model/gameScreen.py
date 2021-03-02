import pygame
from Gorillas.ui.model.model import Model
from Gorillas.color import Color
from Gorillas.ui.model.elements.sprites.sun import Sun
from Gorillas.Backend.Controllers.GameController import GameController


class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE

    def __init__(self, screen_size, player_1_id, player_2_id):
        super(GameScreenModel, self).__init__(self.BACKGROUND_COLOR)
        game_controller = GameController(player_1_id, player_2_id, screen_size)
        game_state = game_controller.next_frame()

        # Create the background
        background = pygame.Surface(screen_size)
        background = background.convert()
        background.fill(self.BACKGROUND_COLOR)
        # Create the Sun object. Won't move.
        sun_width = screen_size[0] / 20
        sun_height = screen_size[1] / 30
        sun_x_pos = (screen_size[0] - sun_width) / 2
        sun_y_pos = (screen_size[1] - sun_height) / 10
        sun = Sun(sun_width, sun_height, sun_x_pos, sun_y_pos)

