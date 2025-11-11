import math
from random import randint
import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 80

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


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450 ) :
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = GAME_COLORS[randint(0,5)]
        self.live = 30

    def move(self) :
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.vy <= -1 or self.vy >= 1 or self.y < 590:
            self.vy -= 1
            if self.x+self.r >= WIDTH or self.x-self.r <= 0 :
                self.vx *= -0.8
            if self.y+self.r >= HEIGHT or self.y-self.r <= 0 :
                self.vy *= -0.8
        else:
            self.y=585
            self.vy=0
            self.vx=0


    def draw(self) :
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest( self, obj ) :
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r+obj.r)**2 :
            return True
        return False


class Gun :
    def __init__( self, screen ) :
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.length = 30
        self.width = 10

    def fire2_start( self, event ) :
        self.f2_on = 1

    def fire2_end( self, event ) :
        """Выстрел мячом.5
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global new_ball
        new_ball = Ball(self.screen)
        new_ball.vx = self.f2_power*math.cos(math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x)))
        new_ball.vy = - self.f2_power*math.sin(math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x)))
        self.f2_on = 0
        self.f2_power = 10

    def targetting( self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((450-event.pos[1])/(event.pos[0]-20)) if event.pos[0]-20 != 0 else math.pi
        self.color = GREY

    def draw( self ) :
        a = self.length+self.f2_power
        b = self.width/2
        pygame.draw.polygon(self.screen, self.color,
        ((20-b*math.sin(self.an),450-b*math.cos(self.an)), (20+b*math.sin(self.an),450+b*math.cos(self.an)),
        (20+b*math.sin(self.an)+a*math.cos(self.an), 450+b*math.cos(self.an)-a*math.sin(self.an)),
        (20-b*math.sin(self.an)+a*math.cos(self.an), 450-b*math.cos(self.an)-a*math.sin(self.an))))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 30:
                self.f2_power += 1


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.vx = randint(-10,10)
        self.vy = randint(-10,10)

    def new_target( self ) :
        """ Инициализация новой цели. """
        x = self.x = randint(100, 750)
        y = self.y = randint(50, 500)
        r = self.r = randint(20, 50)
        color = self.color = GAME_COLORS[randint(1,5)]
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)

    def hit( self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw( self ) :
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )    
     

    def move( self ) :
        self.x += self.vx
        self.y += self.vy
        if self.x+self.r >= WIDTH or self.x-self.r <= 0 :
            self.vx *= -1
        if self.y+self.r >= HEIGHT or self.y-self.r <= 0 :
            self.vy *= -1


new_ball = Ball(screen,-600,-600)

gun = Gun(screen)
target1 = Target(screen)
target2 = Target(screen)
target1.new_target()
target2.new_target()
finished = False

while not finished :
    pygame.time.Clock().tick(FPS)

    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()

    new_ball.draw()

    score_display = pygame.font.Font(None, 50).render(str(target1.points+target2.points), True, (0, 0, 0))
    screen.blit(score_display, (10, 10))
    pygame.display.update()

    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    target1.move()
    target2.move()

    new_ball.move()
    for target in target1, target2:
        if new_ball.hittest(target) and target.live:
            # target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()