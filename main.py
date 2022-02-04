import pygame
from sys import exit

pygame.init()

# Colors
WHITE = (255, 255, 255)
# Set up the screen
SCREEN = pygame.display.set_mode([800, 600])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    SCREEN.fill(WHITE)

    pygame.display.update()

pygame.quit()
