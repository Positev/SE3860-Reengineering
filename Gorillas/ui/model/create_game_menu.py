import operator
from typing import Union

import pygame
import pygame_gui
import utils
from pygame_gui.core.interfaces import IContainerLikeInterface
from ui.model.gameScreen import GameScreenPanel


class NamePanel(pygame_gui.elements.ui_panel.UIPanel):
    _PANEL_SIZE = (300, 80)

    def __init__(self, player_num: int, panel_pos: (int, int),
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface,
                 container: Union[IContainerLikeInterface, None] = None):
        self._rect = pygame.Rect(panel_pos, self._PANEL_SIZE)
        super(NamePanel, self).__init__(self._rect, 0, manager, container=container)
        self._PLAYER_LABEL_RECT = pygame.Rect(110, 10, 80, 20)
        self._NAME_LABEL_RECT = pygame.Rect(10, 30, 40, 20)
        self._NAME_BOX_RECT = pygame.Rect(50, 30, 210, 20)

        self.player_label = pygame_gui.elements.UILabel(relative_rect=self._PLAYER_LABEL_RECT,
                                                        text="Player " + str(player_num) + ": ",
                                                        manager=manager,
                                                        container=self)

        self.name_label = pygame_gui.elements.UILabel(relative_rect=self._NAME_LABEL_RECT,
                                                      text="Name:",
                                                      manager=manager,
                                                      container=self)

        self.name_box = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=self._NAME_BOX_RECT,
                                                                               manager=manager,
                                                                               container=self)


class SettingsPanel(pygame_gui.elements.ui_panel.UIPanel):
    _PANEL_SIZE = (300, 100)

    def __init__(self, panel_pos: (int, int),
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface,
                 container: Union[IContainerLikeInterface, None] = None):
        self._rect = pygame.Rect(panel_pos, self._PANEL_SIZE)
        super(SettingsPanel, self).__init__(self._rect, 0, manager, container=container)

        self._GRAVITY_LABEL_RECT = pygame.Rect(5, 10, 80, 20)
        self._GRAVITY_BOX_RECT = pygame.Rect(85, 10, 210, 20)

        self._SCORE_LABEL_RECT = pygame.Rect(5, 50, 80, 20)
        self._SCORE_BOX_RECT = pygame.Rect(85, 50, 210, 20)

        self.gravity_label = pygame_gui.elements.UILabel(relative_rect=self._GRAVITY_LABEL_RECT,
                                                         text="Gravity:",
                                                         manager=manager,
                                                         container=self)

        self.gravity_box = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=self._GRAVITY_BOX_RECT,
                                                                                  manager=manager,
                                                                                  container=self)
        self.gravity_box.set_allowed_characters("numbers")
        self.gravity_box.allowed_characters.append('.')

        self.score_label = pygame_gui.elements.UILabel(relative_rect=self._SCORE_LABEL_RECT,
                                                       text="Score:",
                                                       manager=manager,
                                                       container=self, )

        self.score_box = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=self._SCORE_BOX_RECT,
                                                                                manager=manager,
                                                                                container=self)
        self.score_box.set_allowed_characters("numbers")


class CreateGameMenu(pygame_gui.elements.ui_panel.UIPanel):
    """A menu for creating a game of Gorillas"""

    PLAYER_ONE_SETTING_POS = (0, 0)
    PLAYER_TWO_SETTING_POS = (300, 0)
    SETTING_POS = (0, 100)

    def __init__(self, parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface):
        self._rect = pygame.rect.Rect(0, 0, 600, 400)
        self._parent_rect = parent_rect
        super(CreateGameMenu, self).__init__(self._rect, 0, manager)
        self._START_BUTTON_RECT = pygame.Rect(0, 225, 240, 60)
        self.player_one_settings_panel = NamePanel(1, self.PLAYER_ONE_SETTING_POS, manager=manager, container=self)
        self.player_two_settings_panel = NamePanel(2, self.PLAYER_TWO_SETTING_POS, manager=manager, container=self)
        self.settings_panel = SettingsPanel(self.SETTING_POS, manager=manager, container=self)
        self.settings_panel.set_relative_position(
            (self._rect.centerx - self.settings_panel.relative_rect.centerx, self.settings_panel.relative_rect.y))

        self.start_button = pygame_gui.elements.UIButton(relative_rect=self._START_BUTTON_RECT,
                                                         text="Start",
                                                         container=self,
                                                         manager=manager)
        self.start_button.set_relative_position(
            (self._rect.width/2 - self.start_button.relative_rect.centerx, self.start_button.relative_rect.y))

        self.set_relative_position(tuple(map(operator.sub, parent_rect.center, self._rect.center)))

    def update(self, time_delta: float):
        super().update(time_delta)
        if self.player_one_settings_panel.name_box.get_text() == self.player_two_settings_panel.name_box.get_text() \
                or self.player_one_settings_panel.name_box.get_text() == "" \
                or self.player_two_settings_panel.name_box.get_text() == "" \
                or not utils.isfloat(self.settings_panel.gravity_box.get_text()) \
                or not utils.isint(self.settings_panel.score_box.get_text()) \
                or float(self.settings_panel.gravity_box.get_text()) <= 0 \
                or int(self.settings_panel.score_box.get_text()) <= 0:
            self.start_button.disable()
        else:
            self.start_button.enable()

    def process_event(self, event: pygame.event.Event) -> bool:
        """
        Process the start button
        :param event: The event to process.
        :return: Should return True if this element makes use of this event.
        """
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                                         {"Change Model": GameScreenPanel(
                                                             self.player_one_settings_panel.name_box.get_text(),
                                                             self.player_two_settings_panel.name_box.get_text(),
                                                             float(self.settings_panel.gravity_box.get_text()),
                                                             int(self.settings_panel.score_box.get_text()),
                                                             self._parent_rect, self.ui_manager)}))
                    return True
        return False
