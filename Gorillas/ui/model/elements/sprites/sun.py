import pygame
from pygame.transform import scale


class Sun(pygame.sprite.Sprite):
    """A class to store information on the sun"""

    def __init__(self, width, height, x_pos, y_pos):
        super(Sun, self).__init__()

        # Create Rect
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.pos = [x_pos, y_pos]
        self.size = [width, height]
        # Create default image
        self.image = pygame.image.load("Sprites/Sun/sun_doug_2.png")
        self.image = scale(self.image, (int(width), int(height)))

    def sun_collide(self, projectile):
        # Return true if the projectile is colliding with the sun at the time
        if pygame.sprite.collide_rect(projectile, self):
            return True
        return False

