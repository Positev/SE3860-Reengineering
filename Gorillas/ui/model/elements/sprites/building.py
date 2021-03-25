import pygame


class Building(pygame.sprite.Sprite):
    WINDOW_COLOR = (192, 192, 192)

    def __init__(self, color, pos, size):
        super(Building, self).__init__()

        self.image = pygame.Surface(size)
        self.rect = (pos[0], pos[1], size[0], size[1])
        self.image.fill(color)
        self.size = size
        self.pos = pos

    def create_windows(self):
        # Let's see if making the windows this way is a possibility
        num_horizontal = random.randint(3, 7)
        num_vertical = random.randint(4, 8)
        window_size = (self.size[0] / num_horizontal, self.size[1] / num_vertical)
        window_pos = (self.pos[0] + window_size[0], self.pos[1] + window_size[1])
        max_x = self.pos[0] + self.size[0]
        max_y = self.pos[1] + self.size[1]

        while window_pos[1] < max_y:
            while window_pos[0] < max_x:
                window_rect = (window_pos[0], window_pos[1], window_size[0], window_size[1])
                pygame.draw.rect(self.image, WINDOW_COLOR, window_rect)
                window_pos[0] += window_size[0] * 2

            window_pos[0] = self.pos[0] + window_size[0]
            window_pos[1] += window_size[1] * 2

