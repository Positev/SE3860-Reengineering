import pygame


class Presenter:
    def __init__(self, screen_size, model):
        self.model = model
        self.running = False
        self.view = pygame.display

    def update_sprites(self):
        for sprite in self.model.mouseSprites:
            command = sprite.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
                for mouseSprite in self.model.sprites.get("mouse"):
                    mouseSprite.handle_event(event)
            elif event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.running = True
        self.view.get_surface().fill(self.model.background_color)
        while self.running:
            for spriteGroup in self.model.sprites.values():
                spriteGroup.draw(self.view.get_surface())
            self.handle_events()
            self.view.update()
