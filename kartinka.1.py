import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1200))
screen.fill((112, 128, 144)) 

# Фон и земля
rect(screen, (52, 80, 70), (0, 685, 1000, 600))  
rect(screen, (146, 175, 151), (-15, 685, 900, 600), 5)  

# Линия горизонта
rect(screen, (255, 255, 255), (0, 685, 800, 2))

# Здания 
rect(screen, (118, 167, 161), (50, 100, 140, 800))
rect(screen, (124, 162, 139), (250, 100, 140, 800))
rect(screen, (100, 140, 144), (170, 150, 140, 800))
rect(screen, (70, 130, 180), (620, 50, 140, 650))
rect(screen, (105, 105, 105), (570, 110, 140, 650))

# Туман
ellipse(screen, (140, 150, 160), (50, 200, 700, 120))
ellipse(screen, (130, 140, 155), (150, 350, 500, 80))

# Светлое пятно под машиной
ellipse(screen, (100, 120, 110), (500, 750, 300, 150))

# Тени.1
ellipse(screen, (80, 100, 90), (100, 750, 120, 40))
ellipse(screen, (80, 100, 90), (200, 730, 100, 35))
ellipse(screen, (80, 100, 90), (280, 720, 80, 30))

# Тени.2
ellipse(screen, (90, 110, 100), (550, 800, 100, 30))
ellipse(screen, (90, 110, 100), (620, 820, 80, 25))

# Корпус машины
rect(screen, (0, 150, 255), (580, 850, 200, 60))

# Кабина
rect(screen, (0, 150, 255), (590, 800, 180, 50))

# Окна
rect(screen, (180, 220, 255), (600, 810, 70, 30))
rect(screen, (180, 220, 255), (700, 810, 60, 30))

# Колёса
circle(screen, (0, 0, 0), (620, 910), 25)
circle(screen, (0, 0, 0), (740, 910), 25)

# Диски колёс
circle(screen, (100, 100, 100), (620, 910), 12)
circle(screen, (100, 100, 100), (740, 910), 12)

# Труба
rect(screen, (40, 40, 40), (580, 880, 20, 15))

pygame.display.update()

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()