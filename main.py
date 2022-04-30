from button import Button
from heading import TextHeading
import pygame
import time
import random

pygame.init()
# colors in rbg
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_colour = (81, 94, 115)

BG = pygame.image.load("assets/poly.png")
pygame.display.set_caption("")
window = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
icon = pygame.image.load("../SortingAlgorithmVisualizer/assets/icon32.png")
pygame.display.set_icon(icon)

arr = [255, 215, 250, 140, 460, 495, 125, 340, 85, 280, 285, 365, 260, 90, 155, 310, 480, 445, 400, 325, 15, 5, 120,
       500,
       265, 470, 305, 65, 25, 100, 150, 225, 10, 385, 220, 185, 35, 20, 410, 135, 235, 195, 355, 115, 190, 130, 180,
       275,
       405, 270, 300, 430, 440, 290, 395, 455, 210, 315, 360, 390, 110, 95, 55, 420, 370, 465, 240, 375, 415, 475, 80,
       50,
       450, 145, 70, 435, 200, 205, 380, 30, 245, 350, 320, 425, 45, 165, 60, 175, 335, 40, 295, 485, 330, 105, 170,
       345,
       75, 230, 490, 160]

arr_sorted = sorted(arr)


def visualizer(arr, j=None):
    for i in range(len(arr)):
        if j == i:
            pygame.draw.rect(window, RED, ((i * 8) + 25, (window.get_height() - 10 - arr[i]), 3, arr[i] + 4))
        elif arr[i] == arr_sorted[i]:
            pygame.draw.rect(window, GREEN, ((i * 8) + 25, (window.get_height() - 10 - arr[i]), 3, arr[i] + 4))
        else:
            pygame.draw.rect(window, BLACK, ((i * 8) + 25, (window.get_height() - 10 - arr[i]), 3, arr[i] + 4))
    pygame.display.update()


def bubble_sort(arr):
    pygame.display.set_caption("Bubble Sort")
    clock.tick(60)
    visualizer(arr)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            window.fill(BG_colour)
            if arr[j] > arr[j + 1]:
                # cool python one liner
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualizer(arr, j + 1)
                pygame.display.update()
    visualizer(arr)
    time.sleep(0.006)
    pygame.display.set_caption("")


def insertion_sort(arr):
    pygame.display.set_caption("Insertion Sort")
    visualizer(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            window.fill(BG_colour)
            arr[j + 1] = arr[j]
            time.sleep(0.002)
            visualizer(arr, j + 1)
            j -= 1
        arr[j + 1] = key
    window.fill(BG_colour)
    visualizer(arr)
    pygame.display.update()
    time.sleep(0.18)
    pygame.display.set_caption("")


def selection_sort(arr):
    pygame.display.set_caption("Selection Sort")
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            time.sleep(0.001)
            window.fill(BG_colour)
            visualizer(arr, j=j)
            if arr[j] < arr[min_idx]:
                min_idx = j
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
        if arr == arr_sorted:
            time.sleep(0.0045)
            pygame.display.set_caption("")
            return


def cocktail_sort(arr):
    pygame.display.set_caption("Cocktail Sort")
    size = len(arr)
    swapped = True
    start = 0
    end = size - 1
    visualizer(arr)
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                time.sleep(0.001)
                window.fill(BG_colour)
                visualizer(arr, j=i)
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                time.sleep(0.001)
                swapped = True
        start = start + 1
    time.sleep(0.18)
    pygame.display.set_caption("")

# main loop
def main_menu():
    run = True
    viz_head = TextHeading("Algo Visualizer", 70, 240, 20, 440, 100, (69, 73, 125))
    bubble_sort_button = Button((67, 135, 187), 345, 200, 235, 60, 45, 'Bubble Sort')
    selection_sort_button = Button((67, 135, 187), 345, 275, 235, 60, 45, 'Selection Sort')
    insertion_sort_button = Button((67, 135, 187), 345, 350, 235, 60, 45, 'Insertion Sort')
    cocktail_sort_button = Button((67, 135, 187), 345, 425, 235, 60, 45, 'Cocktail Sort')

    while run:
        clock.tick(30)
        window.blit(BG, (0, 0))
        bubble_sort_button.draw_button(window, BLACK)
        selection_sort_button.draw_button(window, BLACK)
        insertion_sort_button.draw_button(window, BLACK)
        cocktail_sort_button.draw_button(window, BLACK)
        viz_head.draw_text_box(window)
        pygame.display.update()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # reshuffles array for every button press
                random.shuffle(arr)
                if bubble_sort_button.is_above(mouse_pos):
                    bubble_sort(arr)
                elif selection_sort_button.is_above(mouse_pos):
                    selection_sort(arr)
                elif insertion_sort_button.is_above(mouse_pos):
                    insertion_sort(arr)
                elif cocktail_sort_button.is_above(mouse_pos):
                    cocktail_sort(arr)

            if event.type == pygame.MOUSEMOTION:
                bubble_sort_button.color = (4, 60, 89) if bubble_sort_button.is_above(mouse_pos) else (67, 135, 187)
                selection_sort_button.color = (4, 60, 89) if selection_sort_button.is_above(mouse_pos) else (
                67, 135, 187)
                insertion_sort_button.color = (4, 60, 89) if insertion_sort_button.is_above(mouse_pos) else (
                67, 135, 187)
                cocktail_sort_button.color = (4, 60, 89) if cocktail_sort_button.is_above(mouse_pos) else (67, 135, 187)


# starts execution of program
if __name__ == "__main__":
    main_menu()
