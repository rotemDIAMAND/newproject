import random
import pygame
import consts


mines = []
flag = []


def create_screen():
    screen = []
    tuple_coordinates = []
    for row in range(consts.SCREEN_WIDTH):
        for col in range(consts.SCREEN_HEIGHT):
            tuple_coordinates.append((row, col))
        screen.append(tuple_coordinates)
        tuple_coordinates = []
    return screen


def solider_flag_all(x, y, place, screen):
    d_soldier_flag = []
    row1 = []
    for col in range(y):
        for row in range(x):
            if place[0] + col > len(screen) or place[1] + row > len(screen[col]):
                return [-1]
            row1.append((place[0] + col, place[1] + row))
        d_soldier_flag.append(row1)
        row1 = []
    return d_soldier_flag


def random_mines(mines):
    for i in range(20):
        x = random.randrange(0, 48)
        y = random.randrange(0, 23)
        mines.append((x, y))
        screen = create_screen()
        d_soldier_flag = solider_flag_all(4, 2, (0, 0), screen)
        check_not_touch(mines, d_soldier_flag, i, screen)
        d_soldier_flag = solider_flag_all(4, 3, consts.FLAG_X_Y, screen)
        check_not_touch(mines, d_soldier_flag, i, screen)


def check_not_touch(mines, d_soldier_flag, i, screen):
    for row in range(len(d_soldier_flag)):
        for col in range(len(d_soldier_flag[row])):
            while mines[i] == d_soldier_flag[row][col] or mines[i][0] + 3 > len(screen):
                x = random.randrange(0, 48)
                y = random.randrange(0, 23)
                mines[i] = (x, y)

