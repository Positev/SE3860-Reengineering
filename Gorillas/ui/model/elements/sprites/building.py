import pygame
import random

class Building(pygame.sprite.Sprite):
    WINDOW_COLOR = (192, 192, 192)

    def __init__(self, color, pos, size):
        super(Building, self).__init__()

        self.image = pygame.Surface(size)
        self.rect = (pos[0], pos[1], size[0], size[1])
        self.image.fill(color)
        self.size = size
        self.pos = pos



