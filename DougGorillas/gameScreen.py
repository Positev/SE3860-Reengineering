import pygame
from model import Model
from color import Color
from Backend.Controllers.GameController import GameController
from Backend.Data.GameState import GameState

class GameScreenModel(Model):
    """The main screen of the game"""

    BACKGROUND_COLOR = Color.BLUE

    def __init__(self):
        game_controller = GameController()
        game_state = game_controller.next_frame()
