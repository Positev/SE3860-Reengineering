import pygame

from Gorillas.ui.model.elements.button import Button
from Gorillas.ui.model.elements.edit_box import EditBox
from Gorillas.ui.model.elements.text_box import TextBox
from Gorillas.ui.model.model import Model
from Gorillas.ui.model.gameScreen import GameScreenModel
from Gorillas.color import Color
import Gorillas.utils


class CreateGameMenu(Model):
    """A menu for creating a game of Gorillas"""

    BACKGROUND_COLOR = Color.WHITE
    BUTTON_HEIGHT = 80
    LABEL_FONT_SIZE = 24
    LABEL_WIDTH = 175
    PLAYER_ONE_LABEL_TEXT = "Player 1:"
    PLAYER_TWO_LABEL_TEXT = "Player 2:"
    GRAVITY_LABEL_TEXT = "Gravity:"
    SCORE_LABEL_TEXT = "Score to Win:"
    START_GAME_BUTTON_TEXT = "Start Game"

    MENU_TEXT_HEIGHT = 120

    def __init__(self, screen_size):
        """Initializes the menu"""
        super(CreateGameMenu, self).__init__(self.BACKGROUND_COLOR)
        self.screen_size = screen_size
        self.buttons = list()
        self.edit_boxes = list()
        self.render.append(pygame.sprite.Group())
        self.label_font = pygame.font.Font(pygame.font.get_default_font(), self.LABEL_FONT_SIZE)
        self.label_size = (self.LABEL_WIDTH, pygame.font.Font.size(self.label_font, self.PLAYER_ONE_LABEL_TEXT)[1])

        # Player One label with Edit Box
        player_one_label_pos = (screen_size[0] / 4 - self.LABEL_WIDTH, screen_size[1] / 4)
        self.player_one_label = TextBox(self.label_font, self.label_size, player_one_label_pos,
                                        text=self.PLAYER_ONE_LABEL_TEXT)
        player_one_edit_box_pos = (player_one_label_pos[0] + self.LABEL_WIDTH, player_one_label_pos[1])
        self.player_one_edit_box = EditBox(self.label_font, self.label_size, player_one_edit_box_pos,
                                           back_ground_color=Color.DARK_GRAY)
        self.edit_boxes.append(self.player_one_edit_box)
        self.render[0].add(self.player_one_label)
        self.render[0].add(self.player_one_edit_box)

        # Player Two Label with Edit Box
        player_two_label_pos = (screen_size[0] - (screen_size[0] / 4) - self.LABEL_WIDTH, screen_size[1] / 4)
        self.player_two_label = TextBox(self.label_font, self.label_size, player_two_label_pos,
                                        text=self.PLAYER_TWO_LABEL_TEXT)
        player_two_edit_box_pos = (player_two_label_pos[0] + self.LABEL_WIDTH, player_two_label_pos[1])
        self.player_two_edit_box = EditBox(self.label_font, self.label_size, player_two_edit_box_pos,
                                           back_ground_color=Color.LIGHT_GRAY)
        self.edit_boxes.append(self.player_two_edit_box)
        self.render[0].add(self.player_two_label)
        self.render[0].add(self.player_two_edit_box)

        # Gravity Label with Edit Box
        gravity_label_pos = (screen_size[0] / 2 - self.LABEL_WIDTH, screen_size[1] / 2)
        self.gravity_label = TextBox(self.label_font, self.label_size, gravity_label_pos,
                                     text=self.GRAVITY_LABEL_TEXT)
        gravity_edit_box_pos = (gravity_label_pos[0] + self.LABEL_WIDTH, gravity_label_pos[1])
        self.gravity_edit_box = EditBox(self.label_font, self.label_size, gravity_edit_box_pos,
                                        back_ground_color=Color.LIGHT_GRAY)
        self.edit_boxes.append(self.gravity_edit_box)
        self.render[0].add(self.gravity_label)
        self.render[0].add(self.gravity_edit_box)

        # Score Label with Edit Box
        score_label_pos = (screen_size[0] / 2 - self.LABEL_WIDTH, screen_size[1] / 2 + self.label_size[1] * 2)
        self.score_label = TextBox(self.label_font, self.label_size, score_label_pos,
                                   text=self.SCORE_LABEL_TEXT)
        score_edit_box_pos = (gravity_label_pos[0] + self.LABEL_WIDTH, score_label_pos[1])
        self.score_edit_box = EditBox(self.label_font, self.label_size, score_edit_box_pos,
                                      back_ground_color=Color.LIGHT_GRAY)
        self.edit_boxes.append(self.score_edit_box)
        self.render[0].add(self.score_label)
        self.render[0].add(self.score_edit_box)

        # Start Game Button
        start_game_button_event = pygame.event.Event(pygame.USEREVENT, {"Create Game": None})
        start_game_button_size = (screen_size[0] / 2, self.BUTTON_HEIGHT)
        start_game_button_pos = (
            screen_size[0] / 2 - start_game_button_size[0] / 2, screen_size[1] - screen_size[1] / 4)
        self.start_game_button = Button(start_game_button_event, self.START_GAME_BUTTON_TEXT,
                                        self.label_font, start_game_button_size, start_game_button_pos)
        self.render[0].add(self.start_game_button)
        self.buttons.append(self.start_game_button)

        self.active_editBox = self.player_one_edit_box
        error_label_size = (screen_size[0]/2, self.label_size[1])
        error_label_pos = (screen_size[0]/2 - error_label_size[0] / 2, screen_size[1] - screen_size[1]/4 - error_label_size[1])
        self.error_label = TextBox(self.label_font, error_label_size, error_label_pos)

    def create_game(self):
        """Returns the game menu from the name, gravity, and score text fields
        Throws TypeError if gravity is not a float or if score is not an int"""
        valid_input = True
        player_one_name = self.player_one_edit_box.text
        player_two_name = self.player_two_edit_box.text
        if player_one_name == player_two_name:
            self.error_label.text = "NAMES CANNOT BE EQUAL!"
            valid_input = False
        elif not Gorillas.utils.isfloat(self.gravity_edit_box.text):
            self.error_label.text = "GRAVITY MUST BE FLOAT!"
            valid_input = False
        elif float(self.gravity_edit_box.text) <= 0:
            self.error_label.text = "GRAVITY MUST BE GREATER THAN 0"
            valid_input = False
        elif not Gorillas.utils.isint(self.score_edit_box.text):
            self.error_label.text = "SCORE MUST BE INT!"
            valid_input = False
        elif float(self.score_edit_box.text) <= 0:
            self.error_label.text = "SCORE MUST BE GREATER THAN 0"
            valid_input = False

        if not valid_input:
            self.error_label.update()
            self.render[0].add(self.error_label)
            return self

        gravity = float(self.gravity_edit_box.text)
        score = int(self.score_edit_box.text)
        return GameScreenModel(self.screen_size, player_one_name, player_two_name, gravity, score)


    def get_next_edit_box(self):
        """Sets the active edit box to the next one in the list"""
        index = (self.edit_boxes.index(self.active_editBox) + 1) % len(self.edit_boxes)
        return self.edit_boxes.__getitem__(index)

    def set_edit_box(self, new_edit_box):
        """Sets the active edit box to the given edit box"""
        self.active_editBox.back_ground_color = Color.LIGHT_GRAY
        self.active_editBox.update()
        new_edit_box.back_ground_color = Color.DARK_GRAY
        new_edit_box.update()
        self.active_editBox = new_edit_box

    def do_mouse_event(self, event):
        """Send the event to all the buttons and if the mouse clicks on a text field, set it to the active text box"""
        for button in self.buttons:
            button.handle_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            for edit_box in self.edit_boxes:
                if edit_box.rect.collidepoint(event.pos):
                    self.set_edit_box(edit_box)
                    break

    def do_key_event(self, event):
        """If the key press is enter go to the next text box otherwise send the event to the textbox"""
        if event.key == pygame.K_RETURN:
            self.set_edit_box(self.get_next_edit_box())
        else:
            self.active_editBox.handle_event(event)

    def do_user_event(self, event):
        """If the user event is create game, a game model will try to be added to the event queue"""
        if "Create Game" in event.__dict__:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"Change Model": self.create_game()}))

    def handle_event(self, event):
        """Handle the pygame event"""
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
            self.do_mouse_event(event)
        elif event.type == pygame.USEREVENT:
            self.do_user_event(event)
        elif event.type == pygame.KEYDOWN:
            self.do_key_event(event)
