import sys

import pygame
import pygame_gui
from pygame_gui.core.interfaces import IContainerLikeInterface
from typing import Union

from Gorillas.Backend.Data.GameState import GameState


class EndingScreen(pygame_gui.elements.ui_panel.UIPanel):
    PANEL_SIZE = (300, 200)

    def __init__(self, game_state: GameState,
                 parent_rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface):
        self._rect = parent_rect.copy()
        super(EndingScreen, self).__init__(self._rect, 0, manager)

        label_player1_name = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((350, 250), (200, 20)),
                                                                  text=f"Player: {game_state.gorillas[0].player_id}",
                                                                  manager=manager)
        label_player1_score = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((350, 300), (100, 20)),
                                                                   text=f"Score: {game_state.score.get_score(game_state.gorillas[0].player_id)}",
                                                                   manager=manager)
        label_player2_name = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((750, 250), (200, 20)),
                                                                  text=f"Player: {game_state.gorillas[1].player_id}",
                                                                  manager=manager)
        label_player2_score = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((750, 300), (100, 20)),
                                                                   text=f"Score: {game_state.score.get_score(game_state.gorillas[1].player_id)}",
                                                                   manager=manager)
        label_exit = pygame_gui.elements.ui_label.UILabel(relative_rect=pygame.Rect((470, 700), (300, 20)),
                                                                   text="Press Enter to exit game...",
                                                                   manager=manager)

    def process_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                sys.exit()
                return True



