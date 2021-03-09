import pygame
from color import Color


class Collisions(pygame.sprite.Sprite):
    """This class will handle collisions appearing on the screen"""

    DESTRUCTION_COLOR = Color.BLUE

    def __init__(self, destruction):
        super(Collisions, self).__init__()

        # Create the rect to bound the collision when displayed
        x_pos = destruction.center_x - (destruction.major_axis_dx / 2)
        y_pos = destruction.center_y - (destruction.major_axis_dy / 2)
        self.rect = pygame.Rect(x_pos, y_pos, destruction.major_axis_dx, destruction.major_axis_dy)
        # Create the image of the destruction
        self.image = pygame.Surface((destruction.major_axis_dx, destruction.major_axis_dy))
        self.image = self.image.convert_alpha()
        self.image.fill((0, 0, 0, 0))
        pygame.draw.ellipse(self.image, self.DESTRUCTION_COLOR, self.rect)
