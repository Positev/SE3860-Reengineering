import operator
from typing import Union

import pygame
import pygame_gui
from pygame_gui.core.interfaces import IContainerLikeInterface



class CenterPanel(pygame_gui.elements.ui_panel.UIPanel):
    """The panel to be centered in the main menu containing the Title and buttons"""
    DISPLAY_TITLE = "Main Menu"
    PANEL_SIZE = (400, 400)

    TITLE_SIZE = (400, 200)
    TITLE_POS = (0, 40)
    BUTTON_SIZE = (240, 60)
    BACK_BUTTON_POS = (70, 320)

    def __init__(self, parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface,
                 container: Union[IContainerLikeInterface, None] = None):
        self._rect = pygame.Rect((0, 0), self.PANEL_SIZE)
        super(CenterPanel, self).__init__(self._rect, 0, manager, container=container)

        title_rect = pygame.Rect(self.TITLE_POS, self.TITLE_SIZE)
        self.text = pygame_gui.elements.UITextBox(relative_rect=title_rect,
                                                 html_text="Created By:<br> Adam Huber<br> Trevor Keegan<br> Robert Border<br> Jason Liu",
                                                 manager=manager,
                                                 container=self, object_id="#Credits")

        back_button_rect = pygame.Rect(self.BACK_BUTTON_POS, self.BUTTON_SIZE)
        self.back_button = pygame_gui.elements.UIButton(relative_rect=back_button_rect,
                                                        text="Back",
                                                        container=self,
                                                        manager=manager)

        self.set_relative_position(tuple(map(operator.sub, parent_rect.center, self._rect.center)))


class CreditsScreen(pygame_gui.elements.ui_panel.UIPanel):
    """A Panel for main menu and starting the game"""

    def __init__(self, parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface):
        self._parent_rect = parent_rect
        self._rect = parent_rect.copy()
        super(CreditsScreen, self).__init__(parent_rect, 0, manager)
        self.center_panel = CenterPanel(self._rect, manager, self)

    def process_event(self, event: pygame.event.Event) -> bool:
        from ui.model.main_menu import MainMenuModel
        """
        Process the button events in the menu. Overrides Parent
        :param event: The event to process.
        :return: Should return True if this element makes use of this event.
        """
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.center_panel.back_button:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         {"Change Model": MainMenuModel(
                                                             self._parent_rect, self.ui_manager)}))
                    return True
