import pygame
from color import Color


class Button(pygame.sprite.Sprite):
    """A Button for selecting a menu option"""

    def __init__(self, button_event, text, font, size, pos, default_color=Color.LIGHT_GRAY,
                 hover_color=Color.DARK_GRAY):
        super(Button, self).__init__()
        self.button_event = button_event

        self.font = font
        # Create the font render
        self.textRender = self.font.render(text, True, Color.BLACK)
        self.textRender.get_rect().center = (size[0] // 2, size[1] // 2)

        # Create Hover image
        self.hoverImage = pygame.Surface(size)
        self.hoverImage.fill(hover_color)
        self.hoverImage.blit(self.textRender, self.textRender.get_rect(center=self.hoverImage.get_rect().center))

        # Create default image
        self.defaultImage = pygame.Surface(size)
        self.defaultImage.fill(default_color)
        self.defaultImage.blit(self.textRender, self.textRender.get_rect(center=self.defaultImage.get_rect().center))

        self.image = self.defaultImage
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def handle_event(self, event):
        """Check if the button is being hovered over or clicked"""
        if event.type == pygame.MOUSEMOTION:
            self.update(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                pygame.event.post(self.button_event)

    def update(self, pos):
        """Change the color of the button if its being hover over"""
        if self.image == self.defaultImage and self.rect.collidepoint(pos):
            self.image = self.hoverImage
        elif self.image == self.hoverImage and not self.rect.collidepoint(pos):
            self.image = self.defaultImage
