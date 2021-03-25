import pygame
from color import Color
from ui.model.elements.text_box import TextBox


class EditBox(TextBox):
    """A editable textbox"""
    def __init__(self, font, size, pos, back_ground_color=Color.INVISIBLE, text_color=Color.BLACK, text=''):
        super(EditBox, self).__init__(font, size, pos,
                                      back_ground_color=back_ground_color, text_color=text_color, text=text)

    def handle_event(self, event):
        """Handles the key events by changing its internal text"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.update()
