import pygame
from color import Color


class TextBox(pygame.sprite.Sprite):
    """A Text box sprite"""
    def __init__(self, font, size, pos, back_ground_color=Color.INVISIBLE, text_color=Color.BLACK, text=''):
        super(TextBox, self).__init__()
        self.font = font
        self.back_ground_color = back_ground_color
        self.text_color = text_color
        self.text = text
        self.image = pygame.Surface(size, flags=pygame.SRCALPHA)
        text_render = self.font.render(self.text, True, text_color)
        self.image.fill(back_ground_color)
        text_render.get_rect().center = (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2)
        self.image.blit(text_render, text_render.get_rect(center=self.image.get_rect().center))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        """Recreate the text image"""
        self.image.fill(self.back_ground_color)
        text_render = self.font.render(self.text, True, self.text_color)
        text_render.get_rect().center = (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2)
        self.image.blit(text_render, text_render.get_rect(center=self.image.get_rect().center))
