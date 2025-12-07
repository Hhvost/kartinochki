import pygame
import sys
import math
from random import randint, choice, uniform
from pygame.draw import *

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FPS = 60

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Поймай шарик!")

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

class Ball:
    """Класс для шариков"""
    
    def __init__(self):
        """Инициализация шарика со случайными параметрами"""
        self.radius = randint(20, 60)
        self.x = randint(self.radius, SCREEN_WIDTH - self.radius)
        self.y = randint(self.radius, SCREEN_HEIGHT - self.radius)
        self.color = choice(COLORS)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        
        while self.vx == 0 and self.vy == 0:
            self.vx = randint(-5, 5)
            self.vy = randint(-5, 5)
        self.points = max(10 - self.radius // 10, 1)  # Меньший шарик = больше очков
    
    def draw(self):
        """Рисование шарика на экране"""
        circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def move(self):
        """Движение шарика с отражением от стен"""
        self.x += self.vx
        self.y += self.vy
        
        # Отражение от левой и правой стен
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.vx = -self.vx
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        
        # Отражение от верхней и нижней стен
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.vy = -self.vy
            self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))
    
    def is_clicked(self, mouse_pos):
        """
        Проверка, попал ли игрок в шарик

        """
        distance = math.sqrt((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2)
        return distance <= self.radius


class SquareTarget:
    """Класс для квадратной мишени"""
    
    def __init__(self):
        """Инициализация квадрата"""
        self.size = randint(30, 70)
        self.x = randint(self.size, SCREEN_WIDTH - self.size)
        self.y = randint(self.size, SCREEN_HEIGHT - self.size)
        self.color = choice(COLORS)
        self.vx = uniform(-4, 4)
        self.vy = uniform(-4, 4)
        
        while abs(self.vx) < 1 and abs(self.vy) < 1:
            self.vx = uniform(-4, 4)
            self.vy = uniform(-4, 4)
        self.points = 15  # Квадраты дают больше очков
    
    def draw(self):
        """Рисование квадратной мишени"""
        rect(screen, self.color, 
             (int(self.x - self.size/2), int(self.y - self.size/2), 
              self.size, self.size))
    
    def move(self):
        """Движение квадратной мишени с особым характером движения (зигзаг)"""
        self.x += self.vx
        self.y += self.vy
        
        # Изменение направления движения случайным образом
        if randint(0, 100) < 5:  # 5% шанс изменить направление
            self.vx = uniform(-4, 4)
            self.vy = uniform(-4, 4)
        
        # Отражение от стен с изменением скорости
        if self.x - self.size/2 <= 0 or self.x + self.size/2 >= SCREEN_WIDTH:
            self.vx = -self.vx * uniform(0.8, 1.2)
            self.x = max(self.size/2, min(SCREEN_WIDTH - self.size/2, self.x))
        
        if self.y - self.size/2 <= 0 or self.y + self.size/2 >= SCREEN_HEIGHT:
            self.vy = -self.vy * uniform(0.8, 1.2)
            self.y = max(self.size/2, min(SCREEN_HEIGHT - self.size/2, self.y))
    
    def is_clicked(self, mouse_pos):
        """
        Проверка, попал ли клик в квадратную мишень

        """
        return (abs(mouse_pos[0] - self.x) <= self.size/2 and 
                abs(mouse_pos[1] - self.y) <= self.size/2)


def draw_score(score, time_left):
    """
    Отображение счета и оставшегося времени

    """
    score_text = font.render(f"Счет: {score}", True, WHITE)
    time_text = font.render(f"Время: {time_left} сек", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))


def show_game_over(score):
    """
    Отображение экрана окончания игры
    
    Args:
        score: int - итоговый счет игрока
    """
    screen.fill(BLACK)
    
    game_over_font = pygame.font.Font(None, 72)
    score_font = pygame.font.Font(None, 48)
    restart_font = pygame.font.Font(None, 36)
    
    game_over_text = game_over_font.render("ИГРА ОКОНЧЕНА!", True, RED)
    score_text = score_font.render(f"Ваш счет: {score}", True, YELLOW)
    restart_text = restart_font.render("Нажмите R для перезапуска или ESC для выхода", True, WHITE)
    
    screen.blit(game_over_text, 
                (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//3))
    screen.blit(score_text, 
                (SCREEN_WIDTH//2 - score_text.get_width()//2, SCREEN_HEIGHT//2))
    screen.blit(restart_text, 
                (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT*2//3))
    
    pygame.display.update()
    return True


def main():
   
    # Инициализация игровых переменных
    score = 0
    game_time = 30  # 30 секунд на игру
    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()
    
    # Создание списков шариков и мишеней
    balls = [Ball() for _ in range(5)]  # 5 шариков
    squares = [SquareTarget() for _ in range(3)]  # 3 квадрата

    running = True
    game_active = True
    
    while running:
        current_time = pygame.time.get_ticks()
        dt = (current_time - last_time) / 1000.0 
        last_time = current_time
        
        # Обработка нажатий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r and not game_active:
                    
                    return main()  
            
            elif event.type == pygame.MOUSEBUTTONDOWN and game_active:
                mouse_pos = event.pos
                
                # Проверка попадания по шарикам
                for ball in balls[:]:  
                    if ball.is_clicked(mouse_pos):
                        score += ball.points
                        balls.remove(ball)
                        balls.append(Ball())  # Добавляет новый шарик
                        break  
                
                # Проверка попадания по квадратам
                for square in squares[:]:
                    if square.is_clicked(mouse_pos):
                        score += square.points
                        squares.remove(square)
                        squares.append(SquareTarget())  # Добавляем новый квадрат
                        break
        
        # Обновление времени
        if game_active:
            game_time -= dt
            if game_time <= 0:
                game_active = False
        
        # Отрисовка
        screen.fill(BLACK)
        
        if game_active:
            # Обновление и отрисовка шариков
            for ball in balls:
                ball.move()
                ball.draw()
            
            # Обновление и отрисовка квадратов
            for square in squares:
                square.move()
                square.draw()
            
            # Отображение счета и времени
            draw_score(score, int(game_time))
        else:
            # Показ экрана окончания игры
            if show_game_over(score):
                pass
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()