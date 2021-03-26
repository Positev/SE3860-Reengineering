import pygame


class Banana(pygame.sprite.Sprite):
    """A class for having information on the banana"""

    def __init__(self, size, pos):
        super(Banana, self).__init__()

        # Create rect
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        # Create image
        self.image = pygame.image.load("Sprites/banana.png")
        self.size = size
        self.pos = pos

    def transparent(self):
        """Make the projectile transparent so that it isn't always on-screen"""
        self.image.set_alpha(0)

    def visible(self):
        """Make the projectile visible again"""
        self.image.set_alpha(255)
