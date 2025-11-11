import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 90
screen = pygame.display.set_mode((1200, 800))

colors = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 255), (0, 255, 255)]
score = 0  # начальный счет 0
nob = 5    # кол-во шаров (number of balls)
bo = []    # balls_options = [[скорость, координаты, радиус, цвет],...,[скорост, координаты, радиус, цвет]]

# новый шар со случайными параметрами
def new_ball():
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(20, 40)
    color = colors[randint(0, 5)]
    circle(screen, color, (x, y), r)
    bo.append([[randint(-10, 10), randint(-10, 10)],[x, y],r,color])

# проверка попадания, создание нового шарика
def click(event):
    global score
    for i in range(nob):
        if (bo[i][1][0]-event.pos[0])**2+(bo[i][1][1]-event.pos[1])**2<=(bo[i][2])**2:
            score += 1
            new_ball()
            del bo[i]
            break


def move(screen):
    for i in range(nob):
        if bo[i][1][0]+bo[i][2] >= 1200 or bo[i][1][0]-bo[i][2] <= 0:
            bo[i][0][0] *= -1
        if bo[i][1][1]+bo[i][2] >= 800 or bo[i][1][1]-bo[i][2] <= 0:
            bo[i][0][1] *= -1
        # изменение координат шарика
        bo[i][1][0] += bo[i][0][0]
        bo[i][1][1] += bo[i][0][1]
        circle(screen, bo[i][3], (bo[i][1][0], bo[i][1][1]), bo[i][2])

for i in range(nob):
    new_ball()

finished = False

while not finished:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)  # проверяем, попали ли мы в круг

    move(screen)  # двигаем шарики

    screen.blit(pygame.font.Font(None, 50).render(str(score), True, (255, 255, 255)), (10, 760))
    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()