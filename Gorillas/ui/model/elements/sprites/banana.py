import pygame


class Banana(pygame.sprite.Sprite):
    """A class for having information on the banana"""

    def __init__(self, size, pos):
        super(Banana, self).__init__()

        # Create rect
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        # Create image
        self.defaultImage = pygame.image.Load("/Sprites/banana.png")
