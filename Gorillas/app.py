import pygame
from ui.presenter import Presenter
from ui.model.main_menu import MainMenuModel
from pygame.locals import *


class App:
    def __init__(self):
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 900

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            pass
        main_menu = MainMenuModel(self.size)
        presenter = Presenter(self.size, main_menu)
        presenter.run()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
