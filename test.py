import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1200))
screen.fill((112, 128, 144))


#floor
rect(screen, (52, 80, 70), (0, 685, 1000, 600))
rect(screen, (146, 175, 151), (-15, 685, 900, 600), 5)

#buildings
rect(screen, (118, 167, 161), (50, 100, 140, 800))
rect(screen, (124, 162, 139), (250, 100, 140, 800))
rect(screen, (100, 140, 144), (170, 150, 140, 800))

rect(screen, (70, 130, 180), (620, 50, 140, 650))
rect(screen, (105, 105, 105), (570, 110, 140, 650))

#car



pygame.display.update()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()