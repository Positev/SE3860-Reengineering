import pygame
from ui.model.model import Model
from color import Color
from ui.model.elements.button import Button
from ui.model.elements.text_box import TextBox
from ui.model.create_game_menu import CreateGameMenu


class MainMenuModel(Model):
    """A Button for selecting a menu option
    Function: run"""

    BACKGROUND_COLOR = Color.WHITE

    BUTTON_HEIGHT = 80
    BUTTON_PADDING = 10
    MENU_TEXT = "Doug Gorillas"
    BUTTON_FONT_SIZE = 24
    MENU_TEXT_FONT_SIZE = 72

    MENU_TEXT_HEIGHT = 120

    def __init__(self, screen_size):
        super(MainMenuModel, self).__init__(self.BACKGROUND_COLOR)
        self.button_data = {
            "Start Game": pygame.event.Event(pygame.USEREVENT, {"Change Model": CreateGameMenu(screen_size)}),
            "Credits": pygame.event.Event(pygame.NOEVENT),
            "Quit": pygame.event.Event(pygame.QUIT)
        }
        self.render.append(pygame.sprite.Group())
        self.buttons = list()

        self.button_font = pygame.font.Font(pygame.font.get_default_font(), self.BUTTON_FONT_SIZE)
        self.menu_font = pygame.font.Font(pygame.font.get_default_font(), self.MENU_TEXT_FONT_SIZE)
        # Create menu buttons
        button_size = (screen_size[0] / 2, self.BUTTON_HEIGHT)
        button_x_pos = (screen_size[0] - button_size[0]) / 2
        button_block_size = (self.BUTTON_PADDING * len(self.button_data) + self.BUTTON_HEIGHT * len(self.button_data))
        button_start_position = (screen_size[1] - button_block_size) / 2

        i = 0
        for key, value in self.button_data.items():
            button_y_pos = button_start_position + self.BUTTON_PADDING * i + self.BUTTON_HEIGHT * i
            button = Button(value, key, self.button_font, button_size,
                            (button_x_pos, button_y_pos))
            self.render[0].add(button)
            self.buttons.append(button)
            i += 1

        # Create Menu Text
        menu_text_size = (screen_size[0], pygame.font.Font.size(self.menu_font, "")[1])
        menu_text_pos = ((screen_size[0] - menu_text_size[0]) / 2, button_start_position/2)
        menu_text = TextBox(self.menu_font, menu_text_size, menu_text_pos, text=self.MENU_TEXT)

        self.render[0].add(menu_text)

    def handle_event(self, event):
        """Checks for mouse events and sends to buttons"""
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
            for button in self.buttons:
                button.handle_event(event)
