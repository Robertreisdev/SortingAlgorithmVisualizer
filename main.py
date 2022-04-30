import pygame
import time
import random
from sys import exit

# Colors
#BG = pygame.image.load("poly.png")

BG = (81, 94, 115)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Set up the screen
WIDTH = 900
LENGTH = 600

pygame.init()
SCREEN = pygame.display.set_mode([WIDTH, LENGTH])
pygame.display.set_caption("Algo Viz")

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
            pygame.draw.rect(SCREEN, RED, ((i * 8) + 25, (SCREEN.get_height() - 10 - arr[i]), 3, arr[i] + 4))
        elif arr[i] == arr_sorted[i]:
            pygame.draw.rect(SCREEN, GREEN, ((i * 8) + 25, (SCREEN.get_height() - 10 - arr[i]), 3, arr[i] + 4))
        else:
            pygame.draw.rect(SCREEN, BLACK, ((i * 8) + 25, (SCREEN.get_height() - 10 - arr[i]), 3, arr[i] + 4))

    pygame.display.update()


def bubble_sort(arr):
    visualizer(arr)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            SCREEN.fill(BG)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                time.sleep(0.001)
                visualizer(arr, j + 1)
                pygame.display.update()
    visualizer(arr)
    return arr


def insertion_sort(arr):
    visualizer(arr)
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            SCREEN.fill(BG)
            arr[j + 1] = arr[j]
            time.sleep(0.001)
            visualizer(arr, j + 1)
            j -= 1
        arr[j + 1] = key
    SCREEN.fill(BG)
    visualizer(arr)
    pygame.display.update()


def selectionSort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            time.sleep(0.001)
            SCREEN.fill(BG)
            visualizer(arr, j=i)
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
            if array == sorted(array):
                return
        (array[step], array[min_idx]) = (array[min_idx], array[step])


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    visualizer(arr)
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                time.sleep(0.001)
                SCREEN.fill(BG)
                visualizer(arr, j=i)
                swapped = True

        # if nothing moved, then array is sorted.
        if swapped == False:
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1


SCREEN.fill(BG)
running = True
while running:
    # cocktailSort(arr)
    #selectionSort(arr)
    # insertion_sort(arr)
    bubble_sort(arr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

pygame.quit()
