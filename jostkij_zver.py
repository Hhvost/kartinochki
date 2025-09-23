import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((600, 850))
screen.fill((171, 223, 136))

line_sky_mountains=[(0,262),(72,87),(124,207),(206,112),(358,340),(467,105),(503,147),(600,32)]
line_mountains_land=[(0,448),(28,437),(58,433),(77,433),(128,425),(316,424),(323,427),(326,426),(329,432),(332,434),(333,450),(335,453),(340,465),(350,462),(600,486)]

##небо
polygon(screen,(176,222,234),[(0,0)]+line_sky_mountains+[(600,0)])
lines(screen,(28,27,32),False,line_sky_mountains,4)
line(screen,(28,27,32),[124,207],[206,112],5)
line(screen,(28,27,32),[467,105],[503,147],4)
line(screen,(28,27,32),[503,147],[600,32],5)

##горы
polygon(screen,(180,180,180),line_mountains_land+line_sky_mountains[::-1])
lines(screen,(28,27,32),False,line_mountains_land,1)

##жесткий зверь
#s-размер жесткого зверя
def jostkij_zver(x,y,s,orientation):
    
    #ОСНОВА ЗВЕРЯ
    #тело зверя
    ellipse(screen,(255,255,255),(x,y,135*s,55*s))
    #шея зверя
    ellipse(screen, (255, 255, 255),(x+105*s,y-80*s,40*s,100*s))
    #голова зверя
    ellipse(screen, (255, 255, 255), (x+110*s,y-105*s,50*s,30*s))
    #уши зверя


    #ГЛАЗ ЗВЕРЯ
    #радужка зверя
    ellipse(screen, (230, 129, 255), (x+123*s,y-100*s,25*s,15*s))
    #зрачёк зверя
    ellipse(screen, (0, 0, 0), (x+132*s,y-97*s,9*s,9*s))
    #блик зверя
    ellipse(screen, (255, 255, 255), (x+131*s, y-97, 5*s, 5*s))


    #НОГИ ЗВЕРЯ
    #бедра зверя
    ellipse(screen, (255, 255, 255), (x+8*s,y+25*s,20*s,50*s))
    ellipse(screen, (255, 255, 255), (x+35*s,y+45*s,20*s,50*s))
    ellipse(screen, (255, 255, 255), (x+85*s, y+25*s, 20*s, 50*s))
    ellipse(screen, (255, 255, 255), (x+103*s, y+45*s, 20*s, 50*s))
    #икры зверя
    ellipse(screen, (255, 255, 255), (x+8*s, y+66*s, 20*s, 40*s))
    ellipse(screen, (255, 255, 255), (x+35*s, y+87*s, 20*s, 40*s))
    ellipse(screen, (255, 255, 255), (x+85*s, y+66*s, 20*s, 40*s))
    ellipse(screen, (255, 255, 255), (x+103*s, y+87*s, 20*s, 40*s))
    #копыта зверя
    ellipse(screen, (255, 255, 255), (x+11*s, y+105*s, 20*s, 14*s))
    ellipse(screen, (255, 255, 255), (x+38*s, y+125*s, 20*s, 14*s))
    ellipse(screen, (255, 255, 255), (x+90*s, y+105*s, 20*s, 14*s))
    ellipse(screen, (255, 255, 255), (x+107*s, y+125*s, 20*s, 14*s))

def jostkaja_lujaika(x,y,s):
    #лужайка
    ellipse(screen,(113,201,52),(x-113*s,y-113*s,226*s,226*s))

    def cvetochki():
        #лепестки 2 план
        ellipse(screen, (255, 255, 255), (x, y, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x, y, 20*s, 10*s), 1)

        ellipse(screen, (255, 255, 255), (x-10*s, y+4*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x-10*s, y+4*s, 20*s, 10*s), 1)

        ellipse(screen, (255, 255, 255), (x+13*s, y+4*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x+13*s, y+4*s, 20*s, 10*s), 1)

        #сердцевина
        ellipse(screen, (255, 255, 0), (x+2*s, y+9*s, 25*s, 10*s))
        ellipse(screen, (0, 0, 0), (x+2*s, y+9*s, 25*s, 10*s), 1)
        
        #лепестки передний план
        ellipse(screen, (255, 255, 255), (x-13*s, y+12*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x-13*s, y+12*s, 20*s, 10*s), 1)

        ellipse(screen, (255, 255, 255), (x-2*s, y+14*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x-2*s, y+14*s, 20*s, 10*s), 1)

        ellipse(screen, (255, 255, 255), (x+18*s, y+9*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x+18*s, y+9*s, 20*s, 10*s), 1)

        ellipse(screen, (255, 255, 255), (x+12*s, y+15*s, 20*s, 10*s))
        ellipse(screen, (0, 0, 0), (x+12*s, y+15*s, 20*s, 10*s), 1)
    cvetochki()


jostkaja_lujaika(20,500,0.5)
jostkaja_lujaika(400,700,1)
jostkaja_lujaika(20,500,0.5)
jostkij_zver(75,530,1,1)

pygame.display.update()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()