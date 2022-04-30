import pygame


class TextHeading:
    def __init__(self, text, size, x_cord, y_cord, width, height, colour):
        self.text = text
        self.size = size
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour

    def draw_text_box(self, window):
        pygame.draw.rect(window, self.colour, (self.x_cord, self.y_cord, self.width, self.height), 0)
        font = pygame.font.SysFont('assets/AldotheApache.ttf', self.size)
        text = font.render(self.text, True, (0, 0, 0))
        window.blit(text, (
            self.x_cord + (self.width / 2 - text.get_width() / 2),
            self.y_cord + (self.height / 2 - text.get_height() / 2)))
