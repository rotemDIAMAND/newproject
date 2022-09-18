import pygame
import MineField
import keyboard
import pygame.key
import consts
import Screen

def go_up(soldier_place,screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if col - 1 >= 0:
        soldier_place = screen[row][col - 1]
    return soldier_place

def go_down(soldier_place,screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if col + 1 < 25:
        soldier_place = screen[row][col + 1]
    return soldier_place


def go_left(soldier_place,screen):
    row = soldier_place[0]
    col = soldier_place[1]
    if row - 1 >= 0:
        soldier_place = screen[row - 1][col]
    return soldier_place


def go_right(soldier_place,screen):
    row=soldier_place[0]
    col=soldier_place[1]
    if row + 1 < 50:
         soldier_place = screen[row + 1][col]
    return soldier_place


def show_net():
    Screen.draw_game_night()

def check_soldier_touch_flag(soldier_place):
    if soldier_place == consts.FLAG_X_Y:
            return True
    return False

def check_soldier_touch_mines(soldier_place,mines):
     for i in range(20):
         if soldier_place == mines[i]:
            return True
     return False

def win():
    Screen.draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def lost():
    Screen.draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def handle_user_events(soldier_place,screen,mines):
    keys = pygame.key.get_pressed()
    if keys[consts.UP_KEY]:
        soldier_place = go_up(soldier_place,screen)
    elif keys[consts.DOWN_KEY]:
        soldier_place = go_down(soldier_place,screen)
    elif keys[consts.LEFT_KEY]:
        soldier_place = go_left(soldier_place,screen)
    elif keys[consts.RIGHT_KEY]:
        soldier_place = go_right(soldier_place,screen)
    elif keys[consts.ENTER]:
        show_net()
    if check_soldier_touch_flag(soldier_place):
        win()
    if check_soldier_touch_mines(soldier_place, mines):
        lost()
    return soldier_place






def print_matrix(two_list):
    for row in range(len(two_list)):
        for col in range(len(two_list[row])):
            print(two_list[row][col],end=' ')
        print()

def main():
    soldier = consts.START_SOLDIER
    soldier_place=soldier
    mines = []
    MineField.random_mines(mines)
    screen = []
    tuple_cordinates = []
    for row in range(consts.SCREEN_WIDTH):
        for col in range(consts.SCREEN_HEIGHT):
            tuple_cordinates.append((row, col))
        screen.append(tuple_cordinates)
        tuple_cordinates = []
    pygame.init()
    run = True
    grass=[]
    Screen.random_grass(grass)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            soldier_place = handle_user_events(soldier_place,screen,mines)
            Screen.draw_game(soldier_place[0], soldier_place[1], grass)

    pygame.quit()


if __name__ == '__main__':
    main()




