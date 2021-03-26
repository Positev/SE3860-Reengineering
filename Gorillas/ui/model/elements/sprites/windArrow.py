import pygame
from Backend.Data.Enumerators import WindDirection


class WindArrow(pygame.sprite.Sprite):
    WIND_DEFAULT_WIDTH = 5
    WIND_HEIGHT = 30

    def __init__(self, direction, velocity, screen_size):
        super(WindArrow, self).__init__()

        self.image = pygame.image.load("Sprites/arrow.png")
        wind_width = velocity * self.WIND_DEFAULT_WIDTH
        self.image = pygame.transform.scale(self.image, (wind_width, self.WIND_HEIGHT))
        if direction == WindDirection.LEFT:
            self.image = pygame.transform.flip(self.image, True, False)
        self.wind_pos = ((screen_size[0] - wind_width) / 2, screen_size[1] - self.WIND_HEIGHT)
        self.rect = pygame.Rect(self.wind_pos[0], self.wind_pos[1], wind_width, self.WIND_HEIGHT)
        self.direction = direction