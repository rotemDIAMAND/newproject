import pygame
import consts
import MineField
import Soldier
import random


cell = 20
screen = pygame.display.set_mode((consts.SCREEN_WIDTH * cell, consts.SCREEN_HEIGHT * cell))

GRASS = pygame.image.load("grass.png")
FLAG = pygame.image.load("flag.png")
EXPLOSION = pygame.image.load("explotion.png")
MINE = pygame.image.load("mine.png")


SOLDIER = pygame.transform.scale(Soldier.SOLDIER_IMAGE, (cell * 2, cell * 4))
GRASS_SCREEN = pygame.transform.scale(GRASS, (cell * 2, cell * 2))
FLAG_SCREEN = pygame.transform.scale(FLAG, (cell * 4, cell * 3))
SOLDIER_NIGHT = pygame.transform.scale(Soldier.SOLDIER_MATRIX_IMAGE, (cell * 2, cell * 4))
MINE_SCREEN = pygame.transform.scale(MINE, (cell * 3, cell))
flag_start = False


def start_game(message):
    draw_message(message, consts.LOSE_FONT_SIZE,
                 (255, 255, 255), consts.WIN_LOCATION)


def draw_game(row, col, grass):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_grass(grass)
    screen.blit(FLAG_SCREEN, (consts.X_FLAG_MAX * cell, consts.Y_FLAG_MAX * cell))
    screen.blit(SOLDIER, (row * cell, col * cell))
    pygame.display.update()


def draw_grass(grass):
    for i in range(20):
        screen.blit(GRASS_SCREEN, grass[i])


def lost():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def win():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_game_night(row, col):
    screen.fill(consts.NIGHT_COLOR)
    drawGrid()
    screen.blit(SOLDIER_NIGHT, (row * cell, col * cell))
    for i in range(len(MineField.mines)):
        screen.blit(MINE_SCREEN, (MineField.mines[i][0] * cell, MineField.mines[i][1] * cell))
    pygame.display.update()
    pygame.time.delay(1000)
    return


def drawGrid():
        blockSize = 20  # Set the size of the grid block
        for x in range(0, consts.SCREEN_WIDTH * cell, blockSize):
            for y in range(0, consts.SCREEN_HEIGHT * cell, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, consts.BACKGROUND_COLOR, rect, 1)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
    pygame.display.update()
    pygame.time.delay(1000)


def random_grass(grass):
    for i in range(20):
        x = random.randrange(2, (consts.SCREEN_WIDTH - 2) * cell)
        y = random.randrange(4, (consts.SCREEN_HEIGHT - 2) * cell)
        grass.append((x, y))
