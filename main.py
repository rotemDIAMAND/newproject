import pygame
import random
import keyboard
import pygame.key
import consts
import Screen

def go_up():
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if row-1 > 0:
                soldier_place[row][col]=soldier_place[row - 1][col]


def go_down():
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if row + 1 < 25:
                soldier_place[row][col] = soldier_place[row + 1][col]

def go_left():
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if col + 1 < 50:
                soldier_place[row][col] = soldier_place[row][col + 1]

def go_right():
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if col - 1 > 0:
                soldier_place[row][col] = soldier_place[row][col - 1]

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
            for i in range(20):
                if (row, col) == mines[i]:
                    return True
    return False

def win():
    Screen.draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def lost():
    Screen.draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def handle_user_events():
    for event in pygame.event.get():
        while True:
            if keyboard.is_pressed(consts.UP_KEY):
                go_up()
            elif keyboard.is_pressed(consts.DOWN_KEY):
                go_down()
            elif keyboard.is_pressed(consts.LEFT_KEY):
                go_left()
            elif keyboard.is_pressed(consts.RIGHT_KEY):
                go_right()
            elif keyboard.is_pressed(consts.ENTER):
                show_net()
            if check_soldier_touch_flag(soldier_place):
                win()
            if check_soldier_touch_mines(soldier_place, mines):
                lost()
            break

def random_mines(mines):
    for i in range(20):
        x = random.randrange(0, 51)
        y = random.randrange(0, 25)
        mines.append((x,y))

def main():
    pygame.init()



soldier = consts.START_SOLDIER
soldier_place = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)]
mines = []
random_mines(mines)
print(mines)

if __name__ == '__main__':
    main()



