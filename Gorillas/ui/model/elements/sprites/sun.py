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

    def sun_collide(self, projectile_pos):
        # Return true if the projectile is colliding with the sun at the time
        upper_bound = self.pos[1] - (self.size[1] / 2)
        lower_bound = self.pos[1] + (self.size[1] / 2)
        left_bound = self.pos[0] - (self.size[0] / 2)
        right_bound = self.pos[0] + (self.size[0] / 2)
        # Check if the projectile position is within the bounds of the sun
        if left_bound < projectile_pos[0] < right_bound and upper_bound < projectile_pos[1] < lower_bound:
            return True
        return False

