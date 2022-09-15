import pygame
import consts
import MineField
import Soldier

GRASS = pygame.image.load("grass.png")
FLAG = pygame.image.load("flag.png")
EXPLOSION = pygame.image.load("explotion.png")


screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

def draw_game_normal():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.update()

def draw_game_night():
    screen.fill(consts.NIGHT_COLOR)
    pygame.display.update()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)