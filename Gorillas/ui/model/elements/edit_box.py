import pygame
from Gorillas.color import Color
from Gorillas.ui.model.elements.text_box import TextBox


class EditBox(TextBox):
    """A editable textbox"""
    def __init__(self, font, size, pos, back_ground_color=Color.INVISIBLE, text_color=Color.BLACK, text=''):
        super(EditBox, self).__init__(font, size, pos,
                                      back_ground_color=back_ground_color, text_color=text_color, text=text)

    def update(self):
        """Recreate the text image"""
        self.image.fill(self.back_ground_color)
        text_render = self.font.render(self.text, True, self.text_color)
        text_render.get_rect().center = (self.image.get_size()[0] // 2, self.image.get_size()[1] // 2)
        self.image.blit(text_render, text_render.get_rect(center=self.image.get_rect().center))

    def handle_event(self, event):
        """Handles the key events by changing its internal text"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.update()
