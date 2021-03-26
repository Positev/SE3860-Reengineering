import pygame
import pygame_gui

from ui.presenter import Presenter


class App:
    def __init__(self):
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 900
        self._manager = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._manager = pygame_gui.UIManager(self.size, 'ui/theme.json')

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            pass
        presenter = Presenter(self._manager)
        presenter.run()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
