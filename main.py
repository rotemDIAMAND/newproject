import pygame
import random
import keyboard
import pygame.key
import consts

def go_up():
    pass

def go_down():
    pass

def go_left():
    pass

def go_right():
    pass

def show_net():
    pass

def check_soldier_touch_flag(soldier_place):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if (row,col) == consts.FLAG_X_Y:
                return True
    return False

def check_soldier_touch_mines(soldier_place,mines):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if (row,col) == consts.FLAG_X_Y:
                return True
    return False

while True:
    if keyboard.is_pressed(consts.UP_KEY):
        go_up()
    elif keyboard.is_pressed(consts.DOWN_KEY):
        go_up()
    elif keyboard.is_pressed(consts.LEFT_KEY):
        go_up()
    elif keyboard.is_pressed(consts.RIGHT_KEY):
        go_up()
    elif keyboard.is_pressed(consts.ENTER):
        show_net()
    break


