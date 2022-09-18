import random
import pygame

MINE = pygame.image.load("mine.png")

mines = []


def random_mines(mines):
    for i in range(20):
        x = random.randrange(2, 49)
        y = random.randrange(4, 24)
        mines.append((x,y))