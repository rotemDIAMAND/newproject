import random
import pygame

MINE = pygame.image.load("mine.png")

def random_mines(mines):
    for i in range(20):
        x = random.randrange(2, 51)
        y = random.randrange(4, 25)
        mines.append((x,y))