import pygame
from pygame.transform import scale


class Sun(pygame.sprite.Sprite):
    """A class to store information on the sun"""

    def __init__(self, width, height, x_pos, y_pos):
        super(Sun, self).__init__()

        # Create Rect
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        # Create default image
        self.image = pygame.image.load("Sprites/Sun/sun_doug_2.png")
        # Create optional turn happening image for later development
        # self.thrownImage = pygame.image.load("Sprites/Sun/sun_doug_1.png") #TODO Make Doug sad when banana is thrown
        self.image = scale(self.image, (int(width), int(height)))
        # self.thrownImage = scale(self.thrownImage, (width, height))
