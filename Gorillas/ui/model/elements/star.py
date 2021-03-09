import pygame
from Gorillas.color import Color


class Star(pygame.sprite.Sprite):
    STAR_TEXT = "*"

    def __init__(self, font_size, pos, color=Color.BLACK):
        super(Star, self).__init__()
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        size = pygame.font.Font.size(font, self.STAR_TEXT)
        text_render = font.render(self.STAR_TEXT, True, Color.BLACK)

        self.rect = text_render.get_rect()

        self.image = pygame.Surface(size)
        self.image.fill(Color.INVISIBLE)
        self.image.blit(text_render, self.rect)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
