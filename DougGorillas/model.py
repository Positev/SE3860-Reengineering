import pygame


class Model:
    def __init__(self, background_color):
        self.background_color = background_color
        self.sprites = {
            "mouse": pygame.sprite.Group(),
            "dynamic": pygame.sprite.Group()
        }
