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
    if col + 1 < 21:
        soldier_place = screen[row][col + 1]
    elif row + 4 == 48:
        soldier_place = (row, col)
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
    if row + 1 < 48:
        soldier_place = screen[row + 1][col]
    elif col + 4 == 24:
        soldier_place = (row, col)
    return soldier_place


def show_net(soldier_place):
    Screen.draw_game_night(soldier_place[0], soldier_place[1])

def check_soldier_touch_flag(soldier_place,screen):
    d_soldier = solider_flag_all(4,2,soldier_place, screen)
    d_flag = solider_flag_all(4,3,consts.FLAG_X_Y,screen)
    if d_soldier[0] == -1 or d_flag[0] == -1:
        return False
    for row_soldier in range(len(d_soldier)):
        for col_soldier in range(len(d_soldier[row_soldier])):
            for row_flag in range(len(d_soldier)):
                for col_flag in range(len(d_soldier[row_flag])):
                    if d_soldier[row_soldier][col_soldier] == d_flag[row_flag][col_flag]:
                        return True
    return False

def check_soldier_touch_mines(soldier_place,mines,screen):
     d_soldier=solider_flag_all(4,2,soldier_place,screen)
     if d_soldier[0] == -1:
         return False
     for row in range(len(d_soldier)):
        for i in range(20):
            if d_soldier[row][3] == mines[i]\
                    or d_soldier[row][3] == (mines[i][0]+1,mines[i][1])\
                    or d_soldier[row][3] == (mines[i][0]+2,mines[i][1]):
             return True
     return False

def solider_flag_all(x, y, place, screen):
    d_soldier_flag=[]
    row1=[]
    for col in range(y):
        for row in range(x):
            if place[0]+col>len(screen) or place[1]+row>len(screen[col]):
                return [-1]
            row1.append((place[0]+col,place[1]+row))
        d_soldier_flag.append(row1)
        row1=[]
    return d_soldier_flag


def handle_user_events(soldier_place,screen):
    keys = pygame.key.get_pressed()
    if keys[consts.UP_KEY]:
        soldier_place = go_up(soldier_place,screen)
    elif keys[consts.DOWN_KEY]:
        soldier_place = go_down(soldier_place,screen)
    elif keys[consts.LEFT_KEY]:
        soldier_place = go_left(soldier_place,screen)
    elif keys[consts.RIGHT_KEY]:
        soldier_place = go_right(soldier_place,screen)
    elif keyboard.is_pressed("enter"):
        show_net(soldier_place)
    return soldier_place


def print_matrix(two_list):
    if two_list[0] == -1:
        return
    for row in range(len(two_list)):
        for col in range(len(two_list[row])):
            print(two_list[row][col],end=' ')
        print()

def main():
    soldier = consts.START_SOLDIER
    soldier_place=soldier
    MineField.random_mines(MineField.mines)
    screen = MineField.create_screen()
    pygame.init()
    grass=[]
    Screen.random_grass(grass)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            soldier_place = handle_user_events(soldier_place,screen)
            Screen.draw_game(soldier_place[0], soldier_place[1], grass)
            if check_soldier_touch_flag(soldier_place, screen):
                Screen.win()
                run = False
            if check_soldier_touch_mines(soldier_place, MineField.mines, screen):
                Screen.lost()
                run = False
    pygame.quit()


if __name__ == '__main__':
    main()




