import pygame
import winsound

class Presenter:
    """Handel the display of the view and handle user interactions to the model"""
    def __init__(self, screen_size, model):
        self.model = model
        self.running = False
        self.view = pygame.display

    def handle_events(self):
        """Handle the game events such as quiting, changing the model, or sending events to the model"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.USEREVENT:
                if "Change Model" in event.__dict__:
                    self.model = event.__dict__.get("Change Model")
                else:
                    self.model.handle_event(event)
            else:
                self.model.handle_event(event)

    def run(self):
        """Render all the sprites to the view and handle events"""
        self.running = True
        winsound.PlaySound("sounds\\intro.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        while self.running:
            self.handle_events()
            self.view.get_surface().fill(self.model.background_color)
            for spriteGroup in self.model.render:
                spriteGroup.draw(self.view.get_surface())
            self.model.update()
            self.view.update()
