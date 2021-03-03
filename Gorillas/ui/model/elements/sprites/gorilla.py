import pygame
from pygame.transform import scale


class Gorilla(pygame.sprite.Sprite):
    """A class to store information on the Gorillas"""

    def __init__(self, size, pos):
        super(Gorilla, self).__init__()

        # Create rect
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        # Create images
        self.defaultImage = pygame.image.Load("../../../../Sprites/Doug/doug.png")
        self.leftImage = pygame.image.Load("../../../../Sprites/Doug/dougLeft.png")
        self.rightImage = pygame.image.Load("../../../../Sprites/Doug/dougRight.png")
        scale(self.defaultImage, size, dest_surface=None)
        scale(self.LeftImage, size, dest_surface=None)
        scale(self.RightImage, size, dest_surface=None)
