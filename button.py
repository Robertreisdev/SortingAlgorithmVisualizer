import pygame

pygame.init()
window = pygame.display.set_mode((900, 600))


class Button:
    def __init__(self, color, x_cord, y_cord, width, height, size, text=''):
        self.color = color
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.size = size
        self.text = text

    def draw_button(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x_cord - 2, self.y_cord - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x_cord, self.y_cord, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('assets/AldotheApache.ttf', self.size)
            text = font.render(self.text, True, (0, 0, 0))
            win.blit(text, (
                self.x_cord + (self.width / 2 - text.get_width() / 2),
                self.y_cord + (self.height / 2 - text.get_height() / 2)))

    def is_above(self, mouse_position):
        if self.x_cord < mouse_position[0] < self.x_cord + self.width:
            if self.y_cord < mouse_position[1] < self.y_cord + self.height:
                return True
        return False
