import pygame
from pygame.font import Font

from Gorillas.ui.model.model import Model
from Gorillas.color import Color
from Gorillas.ui.model.elements.sprites.sun import Sun
from Gorillas.ui.model.elements.sprites.gorilla import Gorilla
from Gorillas.Backend.Controllers.GameController import GameController
from Gorillas.ui.model.elements.text_box import TextBox
from Gorillas.ui.model.elements.edit_box import EditBox



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
        self.buildings = ()
        for building in game_state.building:
            self.buildings.add(pygame.Rect(building.x_pos, screen_size[1] - building.height, building.width, building.height))
        # Create player one's gorilla
        self.gorilla_one = self.create_gorilla(game_state.gorillas[0], game_state.building[0])
        # Create player two's gorilla
        self.gorilla_two = self.create_gorilla(game_state.gorillas[1], game_state.building[0])
        """Implement the Input UI and Score UI when Adam has them ready
            Here's more space 
        """
        # Score UI

        ui_font = pygame.font.Font(pygame.font.get_default_font(), 24)

        scoreSize = pygame.font.Font.size(ui_font, "Score: 000")
        player1_score_pos = (0, 0)
        self.player1ScoreBox = TextBox(ui_font, scoreSize, player1_score_pos, text="Score: 0")
        player2_score_pos = (screen_size[0] - scoreSize[0], 0)
        self.player2ScoreBox = TextBox(ui_font, scoreSize, player2_score_pos, text="Score: 0")

        self.render[0].add(self.player1ScoreBox)
        self.render[0].add(self.player2ScoreBox)

        angle_text = "Angle: "
        velocity_text = "Velocity: "
        angle_label_size = pygame.font.Font.size(ui_font, angle_text)
        velocity_label_size = pygame.font.Font.size(ui_font, velocity_text)
        edit_box_size = pygame.font.Font.size(ui_font, "00")
        self.angle_label_positions = (
            (0, player1_score_pos[1] + angle_label_size[1]),
            (screen_size[0] - angle_label_size[0] - edit_box_size[0], player2_score_pos[1] + angle_label_size[1]))
        self.velocity_label_positions = (
            (0, self.angle_label_positions[0][1] + velocity_label_size[1]),
            (screen_size[0] - velocity_label_size[0] - edit_box_size[0], self.angle_label_positions[1][1] + velocity_label_size[1]))
        self.angle_edit_box_positions = (
            (self.angle_label_positions[0][0] + angle_label_size[0], self.angle_label_positions[0][0]),
            (self.angle_label_positions[1][0] + angle_label_size[0], self.angle_label_positions[1][1]))
        self.velocity_edit_box_positions = (
            (self.velocity_label_positions[0][0] + velocity_label_size[0], self.velocity_label_positions[0][1]),
            (self.velocity_label_positions[1][0] + velocity_label_size[0], self.velocity_label_positions[1][1]))

        self.angle_label = \
            TextBox(ui_font, angle_label_size, self.angle_label_positions[1], text=angle_text)
        self.velocity_label = \
            TextBox(ui_font, velocity_label_size, self.velocity_label_positions[1], text=velocity_text)

        self.angle_edit_box = EditBox(ui_font, edit_box_size, self.angle_edit_box_positions[1], back_ground_color=Color.LIGHT_GRAY)
        self.velocity_edit_box = EditBox(ui_font, edit_box_size, self.velocity_edit_box_positions[1], back_ground_color=Color.LIGHT_GRAY)

        # Create the wind arrow
        self.arrow_image = pygame.image.load("../../../../Sprites/arrow.png")
        wind_width = game_state.wind.velocity * self.WIND_DEFAULT_WIDTH
        self.arrow_image = pygame.transform.scale(self.arrow_image, (wind_width, self.WIND_HEIGHT), dest_surface=None)
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
