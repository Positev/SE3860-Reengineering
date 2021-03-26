import winsound

import pygame
from ui.model.main_menu import MainMenuModel


class Presenter:
    """Handel the display of the view and handle user interactions to the model"""

    def __init__(self, gui_manager):
        self._running = False
        self._gui_manager = gui_manager
        self._current_panel = None

    def handle_events(self):
        """Handle the game events such as quiting, changing the model, or sending events to the model"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.USEREVENT and "Change Model" in event.__dict__:
                self._current_panel.kill()
                self._current_panel = event.__dict__.get("Change Model")
            else:
                self._gui_manager.process_events(event)

    def run(self):
        """Render all the sprites to the view and handle events"""
        self._running = True
        clock = pygame.time.Clock()
        self._current_panel = MainMenuModel(pygame.display.get_surface().get_rect(), manager=self._gui_manager)
        winsound.PlaySound("sounds\\intro.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        while self._running:
            time_delta = clock.tick(60) / 1000
            self.handle_events()
            self._gui_manager.update(time_delta)
            screen_surface = pygame.display.get_surface()
            screen_surface.fill(self._gui_manager.get_theme().get_colour('dark_bg'))
            self._gui_manager.draw_ui(screen_surface)
            pygame.display.update()
