import pygame


class Building(pygame.sprite.Sprite):

    def __init__(self, color, pos, size):
        super(Building, self).__init__()

        self.image = pygame.Surface(size)
        self.rect = (pos[0], pos[1], size[0], size[1])
        self.image.fill(color)

