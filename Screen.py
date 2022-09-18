import pygame
import consts
import MineField
import Soldier
import random

cell = 20
screen = pygame.display.set_mode((consts.SCREEN_WIDTH*cell, consts.SCREEN_HEIGHT*cell))

GRASS = pygame.image.load("grass.png")
FLAG = pygame.image.load("flag.png")
EXPLOSION = pygame.image.load("explotion.png")
SOLDIER = pygame.transform.scale(Soldier.SOLDIER_IMAGE,(cell*2,cell*4))
GRASS_SCREEN = pygame.transform.scale(GRASS, (cell, cell))
FLAG_SCREEN = pygame.transform.scale(FLAG, (cell*2, cell*4))



def draw_game(row,col,grass):
    screen.fill(consts.BACKGROUND_COLOR)
    screen.blit(SOLDIER,(row*cell,col*cell))
    screen.blit(FLAG_SCREEN, (consts.X_FLAG_MAX*cell, consts.Y_FLAG_MAX*cell))
    draw_grass(grass)
    pygame.display.update()

def draw_grass(grass):
    for i in range(20):
        screen.blit(GRASS_SCREEN, grass[i])

def draw_game_night():
    screen.fill(consts.NIGHT_COLOR)
    pygame.display.update()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def random_grass(grass):
    for i in range(20):
        x = random.randrange(2, consts.SCREEN_WIDTH*cell)
        y = random.randrange(4, consts.SCREEN_HEIGHT*cell)
        grass.append((x,y))