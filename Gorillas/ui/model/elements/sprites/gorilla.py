import pygame
from pygame.transform import scale


class Gorilla(pygame.sprite.Sprite):
    """A class to store information on the Gorillas"""

    def __init__(self, size, pos):
        super(Gorilla, self).__init__()

        # Create rect
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        # Create images
        self.image = pygame.image.load("Sprites/Doug/doug.png")
        self.leftImage = pygame.image.load("Sprites/Doug/dougLeft.png")
        self.rightImage = pygame.image.load("Sprites/Doug/dougRight.png")
        scale(self.image, (int(size[0]), int(size[1])))
        # scale(self.LeftImage, size)
        # scale(self.RightImage, size)
