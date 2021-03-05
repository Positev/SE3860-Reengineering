import pygame
from Gorillas.ui.model.elements.sprites.windArrow import WindArrow
from Gorillas.ui.model.elements.sprites.banana import Banana
from Gorillas.ui.model.elements.sprites.collisions import Collisions
from Gorillas.ui.model.model import Model
from Gorillas.color import Color
from Gorillas.ui.model.elements.sprites.sun import Sun
from Gorillas.ui.model.elements.sprites.gorilla import Gorilla
from Gorillas.Backend.Controllers.GameController import GameController
from Gorillas.ui.model.elements.text_box import TextBox
from Gorillas.ui.model.elements.edit_box import EditBox
from Gorillas.ui.model.elements.sprites.building import Building
from Gorillas.Backend.Adapters.CoordinateAdapter import CoordinateAdapter


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
        self.game_state = coordinate_adapter.adapt(self.game_controller.next_frame())

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
        for building in self.game_state.building:
            building_pos = (building.x_pos, building.y_pos - building.height)
            building_size = (building.width, building.height)
            new_building = Building(building.color, building_pos, building_size)
            self.render[0].add(new_building)
            self.buildings.append(new_building)
        # Create player one's gorilla
        self.gorilla_one = self.create_gorilla(self.game_state.gorillas[0], self.game_state.building[0],
                                               self.GORILLA_IMAGE)
        self.render[1].add(self.gorilla_one)
        # Create player two's gorilla
        self.gorilla_two = self.create_gorilla(self.game_state.gorillas[1], self.game_state.building[0],
                                               self.GORILLA_IMAGE)
        self.render[1].add(self.gorilla_two)
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

        self.render[2].add(self.player1ScoreBox)
        self.render[2].add(self.player2ScoreBox)

        angle_text = "Angle: "
        velocity_text = "Velocity: "
        angle_label_size = pygame.font.Font.size(ui_font, angle_text)
        velocity_label_size = pygame.font.Font.size(ui_font, velocity_text)
        edit_box_size = pygame.font.Font.size(ui_font, "00")
        self.angle_label_positions = (
            (0, player1_score_pos[1] + scoreSize[1]),
            (screen_size[0] - angle_label_size[0] - edit_box_size[0], player2_score_pos[1] + angle_label_size[1]))
        self.velocity_label_positions = (
            (0, self.angle_label_positions[0][1] + velocity_label_size[1]),
            (screen_size[0] - velocity_label_size[0] - edit_box_size[0],
             self.angle_label_positions[1][1] + velocity_label_size[1]))
        self.angle_edit_box_positions = (
            (self.angle_label_positions[0][0] + angle_label_size[0], self.angle_label_positions[0][1]),
            (self.angle_label_positions[1][0] + angle_label_size[0], self.angle_label_positions[1][1]))
        self.velocity_edit_box_positions = (
            (self.velocity_label_positions[0][0] + velocity_label_size[0], self.velocity_label_positions[0][1]),
            (self.velocity_label_positions[1][0] + velocity_label_size[0], self.velocity_label_positions[1][1]))

        self.angle_label = \
            TextBox(ui_font, angle_label_size, self.angle_label_positions[0], text=angle_text)
        self.velocity_label = \
            TextBox(ui_font, velocity_label_size, self.velocity_label_positions[0], text=velocity_text)

        self.angle_edit_box = EditBox(ui_font, edit_box_size, self.angle_edit_box_positions[0],
                                      back_ground_color=Color.LIGHT_GRAY)
        self.velocity_edit_box = EditBox(ui_font, edit_box_size, self.velocity_edit_box_positions[0],
                                         back_ground_color=Color.LIGHT_GRAY)

        self.render[2].add(self.angle_label)
        self.render[2].add(self.angle_edit_box)
        self.render[2].add(self.velocity_label)
        self.render[2].add(self.velocity_edit_box)

        # Create the wind arrow
        self.wind_arrow = WindArrow(self.game_state.wind.direction, self.game_state.wind.velocity, screen_size)
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

    def move_player_ui(self):
        player = self.game_state._player_turn  # todo change to not use private member
        self.angle_label.rect.topleft = self.angle_label_positions[player]
        self.angle_edit_box.rect.topleft = self.angle_edit_box_positions[player]
        self.velocity_label.rect.topleft = self.velocity_label_positions[player]
        self.velocity_edit_box.rect.topleft = self.velocity_edit_box_positions[player]

    def get_player_throw(self):
        try:
            return int(self.angle_edit_box.text), int(self.velocity_edit_box.text)
        except ValueError:
            return 0, 0  # Todo Change to error message

    def create_gorilla(self, gorilla, building, image):
        """Creates a UI Gorilla object from given data"""
        size = (building.width * 5) / 8
        pos = (gorilla.x_pos - size / 2, gorilla.y_pos - size)
        dimensions = (size, size)
        new_gorilla = Gorilla(dimensions, pos, image)
        return new_gorilla

    def update_frame(self, frame):
        """Updates the background to be a new frame of the game"""
        # Update the gorillas
        if frame.gorillas[0].arm_state == frame.gorillas[0].ArmState.ARM_DOWN:
            self.gorilla_one.image = self.GORILLA_IMAGE
        elif frame.gorillas[0].arm_state == frame.gorillas[0].ArmState.LEFT_ARM_UP:
            self.gorilla_one.image = self.GORILLA_LEFT
        elif frame.gorillas[0].arm_state == frame.gorillas[0].ArmState.RIGHT_ARM_UP:
            self.gorilla_one.image = self.GORILLA_RIGHT

        if frame.gorillas[1].arm_state == frame.gorillas[1].ArmState.ARM_DOWN:
            self.gorilla_two.image = self.GORILLA_IMAGE
        elif frame.gorillas[1].arm_state == frame.gorillas[1].ArmState.LEFT_ARM_UP:
            self.gorilla_two.image = self.GORILLA_LEFT
        elif frame.gorillas[1].arm_state == frame.gorillas[1].ArmState.RIGHT_ARM_UP:
            self.gorilla_two.image = self.GORILLA_RIGHT

        # Update the projectile
        if frame.turn_active():
            projectile_pos = (frame.active_projectiles[0].current_x, frame.active_projectiles[0].current_y)
            self.projectile.rect = pygame.Rect(projectile_pos[0], projectile_pos[1], self.projectile.size[0],
                                               self.projectile.size[1])
            self.projectile.visible()

        # Create collisions if a new collision has appeared
        if self.collision_num < len(frame.destruction):
            new_collision = Collisions(frame.destruction[self.collision_num])
            self.collision_list.add(new_collision)
            self.render[1].add(new_collision)
            self.background.blit(self.collision_list[self.collision_num].image,
                                 self.sollision_list[self.collision_num].rect)
            self.collision_num = self.collision_num + 1

        # Update the wind
        new_width = frame.wind.velocity * self.wind_arrow.WIND_DEFAULT_WIDTH
        self.wind_arrow.image = pygame.transform.scale(self.wind_arrow.image, (new_width, self.wind_arrow.WIND_HEIGHT))
        if self.wind_arrow.direction != frame.wind.direction:
            self.wind_arrow.image = pygame.transform.flip(self.wind_arrow.image, True, False)
        self.wind_arrow.rect = pygame.Rect(self.wind_arrow.wind_pos[0], self.wind_arrow.wind_pos[1], new_width,
                                           self.wind_arrow.WIND_HEIGHT)

        """Room to update UI Elements when working on combining all branches into a coherent branch"""

        # Update the background
        pygame.display.update()
