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


def show_net(soldier_place):
    Screen.draw_game_night(soldier_place[0], soldier_place[1])

def check_soldier_touch_flag(soldier_place):
    if soldier_place == consts.FLAG_X_Y or (consts.X_FLAG_MAX,consts.Y_FLAG_MAX)==soldier_place:
            return True
    return False

def check_soldier_touch_mines(soldier_place,mines,screen):
     print(soldier_place)
     d_soldier=solider_all(soldier_place,screen)
     count = 0
     for i in range(20):
        if soldier_place == mines[i]:
            return True
     return False

def solider_all(soldier_place,screen):
    d_soldier=[]
    row1=[]
    for row in range(2):
        for col in range(4):
            if soldier_place[0]+row>len(screen) or soldier_place[1]+col>len(screen[row]):
                return [-1]
            row1.append((soldier_place[0]+row,soldier_place[1]+col))
        d_soldier.append(row1)
    print_matrix(d_soldier)
    return d_soldier


def handle_user_events(soldier_place,screen,mines,run):
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
    if check_soldier_touch_flag(soldier_place):
        Screen.win()
        run = False
    if check_soldier_touch_mines(soldier_place, mines,screen):
        Screen.lost()
        run = False
    return soldier_place, run






def print_matrix(two_list):
    for row in range(len(two_list)):
        for col in range(len(two_list[row])):
            print(two_list[row][col],end=' ')
        print()

def main():
    soldier = consts.START_SOLDIER
    soldier_place=soldier
    MineField.random_mines(MineField.mines)
    print(MineField.mines)
    screen = []
    tuple_cordinates = []
    for row in range(consts.SCREEN_WIDTH):
        for col in range(consts.SCREEN_HEIGHT):
            tuple_cordinates.append((row, col))
        screen.append(tuple_cordinates)
        tuple_cordinates = []
    pygame.init()
    grass=[]
    Screen.random_grass(grass)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            soldier_place,run = handle_user_events(soldier_place,screen,MineField.mines,run)
            Screen.draw_game(soldier_place[0], soldier_place[1], grass)

    pygame.quit()


if __name__ == '__main__':
    main()




