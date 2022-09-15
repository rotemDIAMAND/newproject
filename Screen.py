import pygame
import consts

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)