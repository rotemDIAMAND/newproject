import pygame

SOLDIER_IMAGE = pygame.image.load("soldier.png")
SOLDIER_HURT_IMAGE = pygame.image.load("injury.png")
SOLDIER_MATRIX_IMAGE = pygame.image.load("soldier_nigth.png")


def go_up(soldier_place, screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if col - 1 >= 0:
        soldier_place = screen[row][col - 1]
    return soldier_place


def go_down(soldier_place, screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if col + 1 < 21:
        soldier_place = screen[row][col + 1]
    elif row + 4 == 48:
        soldier_place = (row, col)
    return soldier_place


def go_left(soldier_place, screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if row - 1 >= 0:
        soldier_place = screen[row - 1][col]
    return soldier_place


def go_right(soldier_place, screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if row + 1 < 48:
        soldier_place = screen[row + 1][col]
    elif col + 4 == 24:
        soldier_place = (row, col)
    return soldier_place