import pygame


class Windows(pygame.sprite.Sprite):
    WINDOW_COLOR = (192, 192, 192)

    def __init__(self, size, pos):
        super(Windows, self).__init__()

        self.image = pygame.Surface(size)
        self.rect = (pos[0], pos[1], size[0], size[1])
        self.image.fill(self.WINDOW_COLOR)
