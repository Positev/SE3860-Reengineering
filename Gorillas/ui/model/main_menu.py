import pygame
import pygame_gui
import operator
from typing import Union
from pygame_gui.core.interfaces import IContainerLikeInterface
from ui.model.create_game_menu import CreateGameMenu


class CenterPanel(pygame_gui.elements.ui_panel.UIPanel):
    """The panel to be centered in the main menu containing the Title and buttons"""
    DISPLAY_TITLE = "Main Menu"
    PANEL_SIZE = (400, 400)

    TITLE_SIZE = (400, 80)
    TITLE_POS = (0, 40)
    BUTTON_SIZE = (240, 60)
    START_BUTTON_POS = (70, 160)
    CREDITS_BUTTON_POS = (70, 240)
    QUIT_BUTTON_POS = (70, 320)

    def __init__(self, parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface,
                 container: Union[IContainerLikeInterface, None] = None):
        self._rect = pygame.Rect((0, 0), self.PANEL_SIZE)
        super(CenterPanel, self).__init__(self._rect, 0, manager, container=container)

        title_rect = pygame.Rect(self.TITLE_POS, self.TITLE_SIZE)
        self.title = pygame_gui.elements.UILabel(relative_rect=title_rect, text="Doug Gorillas", manager=manager,
                                                 container=self, object_id="#Title")

        start_button_rect = pygame.Rect(self.START_BUTTON_POS, self.BUTTON_SIZE)
        self.start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect,
                                                         text="Start Game",
                                                         container=self,
                                                         manager=manager)
        credits_button_rect = pygame.Rect(self.CREDITS_BUTTON_POS, self.BUTTON_SIZE)
        self.credits_button = pygame_gui.elements.UIButton(relative_rect=credits_button_rect,
                                                           text="Credits",
                                                           container=self,
                                                           manager=manager)
        quit_button_rect = pygame.Rect(self.QUIT_BUTTON_POS, self.BUTTON_SIZE)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=quit_button_rect,
                                                        text="Quit",
                                                        container=self,
                                                        manager=manager)

        self.set_relative_position(tuple(map(operator.sub, parent_rect.center, self._rect.center)))


class MainMenuModel(pygame_gui.elements.ui_panel.UIPanel):
    """A Panel for main menu and starting the game"""

    def __init__(self, parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface):
        self._parent_rect = parent_rect
        self._rect = parent_rect.copy()
        super(MainMenuModel, self).__init__(parent_rect, 0, manager)
        self.center_panel = CenterPanel(self._rect, manager, self)

    def process_event(self, event: pygame.event.Event) -> bool:
        """
        Process the button events in the menu. Overrides Parent
        :param event: The event to process.
        :return: Should return True if this element makes use of this event.
        """
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.center_panel.start_button:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         {"Change Model": CreateGameMenu(
                                                             self._parent_rect, self.ui_manager)}))
                    return True
                elif event.ui_element == self.center_panel.credits_button:
                    return True
                    pass
                elif event.ui_element == self.center_panel.quit_button:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                    return True
