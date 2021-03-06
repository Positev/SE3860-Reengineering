import pygame


class Model:
    """A base class for creating a model to render sprites"""
    def __init__(self, background_color):
        self.background_color = background_color
        self.render = list()

    def handle_event(self, event):
        """Handle a given event, to be overloaded"""
        pass

    def update(self):
        """Handle any updates that need to be done on each frame"""
        pass
