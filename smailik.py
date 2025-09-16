import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
#face
circle(screen, (255, 255, 0), (295, 300), 170)
circle(screen, (0,0,0), (295, 300), 170,1)
#mouth
rect(screen,(0,0,0),(200,360,190,30))
#left
circle(screen,(255,0,0),(215,250), 32)
circle(screen,(0,0,0),(215,250), 17)
circle(screen,(0,0,0),(215,250), 32, 1)
#right
circle(screen,(255,0,0),(365,250), 23)
circle(screen,(0,0,0),(365,250), 11)
circle(screen,(0,0,0),(365,250), 23, 1)
#eyebrows
line(screen,(0, 0, 0), [330,235],[400,195], 18)
line(screen,(0, 0, 0),[190,195],[260,235], 18)

pygame.display.update()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()