from typing import Union
import pygame
import pygame_gui
from pygame_gui.core.interfaces import IContainerLikeInterface
from pygame_gui.core import UIElement


class GridPanel(pygame_gui.elements.ui_panel.UIPanel):
    DISPLAY_TITLE = "Main Menu"

    def __init__(self, columns, rows, rect: pygame.Rect,
                 manager: pygame_gui.core.interfaces.manager_interface.IUIManagerInterface,
                 container: Union[IContainerLikeInterface, None] = None,
                 parent_element: UIElement = None
                 ):
        super(GridPanel, self).__init__(rect, 0, manager, container=container, parent_element=parent_element,
                                        anchors={'left': 'left',
                                                 'right': 'right',
                                                 'top': 'top',
                                                 'bottom': 'bottom'})
        self.columns = columns
        self.rows = rows
        self.panels = [[None for i in range(rows)] for j in range(columns)]

        panel_size = (self._rect.size[0] / self.columns, self._rect.size[1] / self.rows)
        for i in range(self.columns):
            for j in range(self.rows):
                panel_pos = (panel_size[0] * i, panel_size[1] * j)
                panel_rect = pygame.Rect(panel_pos, panel_size)
                self.panels[i][j] = pygame_gui.elements.ui_panel.UIPanel(panel_rect, 0, manager, container=self,
                                                                         object_id="#GridPanel",
                                                                         anchors={'left': 'left',
                                                                                  'right': 'right',
                                                                                  'top': 'top',
                                                                                  'bottom': 'top'})

    def build(self):

        """
                start_button_rect = pygame.Rect(0, 0, 100, 20)
                start_button_rect.center = (panel_size[0]/2, panel_size[1]/2)
                start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect,
                                                            text="Hello" + str(i),
                                                            container=self._panels[i][j],
                                                            manager=self._manager,
                                                            anchors={'left': 'left',
                                                                     'right': 'right',
                                                                     'top': 'top',
                                                                     'bottom': 'bottom'})
                                                                     """
