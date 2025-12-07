import math
from random import randint, choice
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

def rnd(a, b):
    return randint(a, b)

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.gravity = 0.5

    def move(self):
        self.vy -= self.gravity
        self.x += self.vx
        self.y -= self.vy
        
        self.live -= 1
        
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.vx = -self.vx * 0.8
            self.x = max(self.r, min(WIDTH - self.r, self.x))
        
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.vy = -self.vy * 0.8
            self.y = max(self.r, min(HEIGHT - self.r, self.y))

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r
        )

    def hittest_circle(self, obj):
        distance = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
        return distance <= (self.r + obj.r)
    
    def hittest_square(self, obj):
        return (abs(self.x - obj.x) <= (self.r + obj.size/2) and 
                abs(self.y - obj.y) <= (self.r + obj.size/2))


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        length = 20 + self.f2_power / 2
        end_x = self.x + length * math.cos(self.an)
        end_y = self.y + length * math.sin(self.an)
        
        pygame.draw.line(
            self.screen,
            self.color,
            (self.x, self.y),
            (end_x, end_y),
            7
        )
        
        pygame.draw.circle(
            self.screen,
            GREY,
            (self.x, self.y),
            15
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        while self.vx == 0 and self.vy == 0:
            self.vx = randint(-2, 2)
            self.vy = randint(-2, 2)

    def new_target(self):
        self.x = rnd(100, WIDTH - 100)
        self.y = rnd(100, HEIGHT - 100)
        self.r = rnd(20, 40)
        self.color = RED
        self.live = 1

    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.vx = -self.vx
            self.x = max(self.r, min(WIDTH - self.r, self.x))
        
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.vy = -self.vy
            self.y = max(self.r, min(HEIGHT - self.r, self.y))

    def hit(self, points=1):
        self.points += points
        return self.points

    def draw(self):
        if self.live:
            pygame.draw.circle(
                self.screen,
                self.color,
                (int(self.x), int(self.y)),
                self.r
            )


class BadTarget:
    """Плохая цель (квадратная), по которой нельзя попадать"""
    
    def __init__(self, screen):
        self.screen = screen
        self.live = 1
        self.new_target()
        self.vx = randint(-3, 3)
        self.vy = randint(-3, 3)
        while self.vx == 0 and self.vy == 0:
            self.vx = randint(-3, 3)
            self.vy = randint(-3, 3)

    def new_target(self):
        self.x = rnd(100, WIDTH - 100)
        self.y = rnd(100, HEIGHT - 100)
        self.size = rnd(25, 35)
        self.color = BLACK  # Черный квадрат - плохая цель
        self.live = 1

    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.x + self.size/2 >= WIDTH or self.x - self.size/2 <= 0:
            self.vx = -self.vx
            self.x = max(self.size/2, min(WIDTH - self.size/2, self.x))
        
        if self.y + self.size/2 >= HEIGHT or self.y - self.size/2 <= 0:
            self.vy = -self.vy
            self.y = max(self.size/2, min(HEIGHT - self.size/2, self.y))

    def hit(self):
        """Попадание квадрат - минус 1 балл"""
        self.live = 0
        return -1  

    def draw(self):
        if self.live:
            pygame.draw.rect(
                self.screen,
                self.color,
                (int(self.x - self.size/2), int(self.y - self.size/2), 
                 self.size, self.size)
            )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)

# 2 шара
targets = [Target(screen) for _ in range(2)]

# 1 квадрат
bad_target = BadTarget(screen)

total_points = 0

font = pygame.font.Font(None, 36)

finished = False

while not finished:
    screen.fill(WHITE)
    
    # Отображает счет
    score_text = font.render(f"Счет: {total_points}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Инструкция
    instruction_text = font.render("Черные квадраты отнимают 1 балл!", True, RED)
    screen.blit(instruction_text, (WIDTH - 400, 10))
    
    gun.draw()
    
    # Рисует шары
    for target in targets:
        target.draw()
    
    # Рисует квадрат
    bad_target.draw()
    
    # Рисует все элементы
    for b in balls:
        b.draw()
    
    pygame.display.update()

    clock.tick(FPS)
    
    # Обработка нажатий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    # Движение шаров
    for b in balls[:]:
        b.move()
        
        if b.live <= 0:
            balls.remove(b)
        else:
            # Проверка попадания в щары
            for target in targets:
                if b.hittest_circle(target) and target.live:
                    target.live = 0
                    points = target.hit()
                    total_points += points
                    target.new_target()
            
            # Проверка попадания в квадрат
            if b.hittest_square(bad_target) and bad_target.live:
                bad_target.live = 0
                penalty = bad_target.hit()
                total_points += penalty  
                bad_target.new_target()
    
    # Движение целей
    for target in targets:
        target.move()
    
    bad_target.move()
    
    gun.power_up()

pygame.quit()
print(f"Игра окончена! Итоговый счет: {total_points}")