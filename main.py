import pygame
import MineField
import keyboard
import pygame.key
import consts
import Screen

def go_up(soldier_place):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if row-1 > 0:
                soldier_place[row][col]=soldier_place[row - 1][col]
    return soldier_place

def go_down(soldier_place):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if row + 1 < 25:
                soldier_place[row][col] = soldier_place[row + 1][col]
    return soldier_place

def go_left(soldier_place,screen):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if col + 1 < 50:
                soldier_place[row][col] = soldier_place[row][col + 1]
    return soldier_place

def go_right(soldier_place,screen):
    for row in range(len(soldier_place)):
        for col in range(len(soldier_place[row])):
            if col - 1 > 0:
                soldier_place[row][col] = soldier_place[row][col - 1]
    return soldier_place

def show_net():
    Screen.draw_game_night()

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






def print_matrix(two_list):
    for row in range(len(two_list)):
        for col in range(len(two_list[row])):
            print(two_list[row][col],end=' ')
        print()

def main():
    pygame.init()
    run = True
    grass=[]
    Screen.random_grass(grass)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            handle_user_events()
        Screen.draw_game(0,0,grass)

    pygame.quit()



soldier = consts.START_SOLDIER
soldier_place = (0,0)
mines = []
MineField.random_mines(mines)
screen = []
tuple_cordinates=[]
for row in range(consts.SCREEN_HEIGHT):
    for col in range(consts.SCREEN_WIDTH):
        tuple_cordinates.append((row,col))
    screen.append(tuple_cordinates)
    tuple_cordinates=[]


if __name__ == '__main__':
    main()




