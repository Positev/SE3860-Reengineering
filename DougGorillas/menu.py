"""from button import Button


def buttonHover():
    pygame.sprite.Group

def run(screen):
    button1 = Button((pygame.display.get_surface().get_height()/2 - 150,pygame.display.get_surface().get_width()/2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                for s in pygame.sprite.Group(button1):
                    button1.hover(event.pos)

        screen.fill((255,255,255))
        screen.blit(button1.surf, button1.pos)
        pygame.display.update()
"""
import pygame
from model import Model
from color import Color
from button import Button
from star import Star


class MainMenuModel(Model):
    """A Button for selecting a menu option
    Function: run"""

    BACKGROUND_COLOR = Color.WHITE
    BUTTON_DATA = {
       "Start Game": pygame.event.Event(pygame.NOEVENT),
       "Credits": pygame.event.Event(pygame.NOEVENT),
       "Quit": pygame.event.Event(pygame.QUIT)
    }
    BUTTON_HEIGHT = 80
    BUTTON_PADDING = 10
    BUTTON_FONT_SIZE = 24

    def __init__(self, screen_size):
        super(MainMenuModel, self).__init__(self.BACKGROUND_COLOR)
        button_size = screen_size[0] / 2
        button_x_pos = (screen_size[0] - button_size) / 2
        button_block_size = (self.BUTTON_PADDING * len(self.BUTTON_DATA) + self.BUTTON_HEIGHT * len(self.BUTTON_DATA))
        button_start_position = (screen_size[1] - button_block_size) / 2

        i = 0
        for key, value in self.BUTTON_DATA.items():
            button_y_pos = button_start_position + self.BUTTON_PADDING * i + self.BUTTON_HEIGHT * i
            button = Button(value, key, self.BUTTON_FONT_SIZE, (button_size, self.BUTTON_HEIGHT),
                            (button_x_pos, button_y_pos))
            self.sprites.get("mouse").add(button)
            i += 1

        self.sprites.get("dynamic").add(Star(20, (50, 50)))
