#индекс

'''import turtle

# Размеры цифр
DIGIT_WIDTH = 40
DIGIT_HEIGHT = 120
GAP = DIGIT_WIDTH // 4  # отступ

def draw_segment(start, end):
    """Рисует один сегмент"""
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()

def draw_digit(x, digit):
    """Рисует цифру в позиции x"""
    # Координаты сегментов (горизонтальные и вертикальные линии)
    segments_coords = {
        'a': ((x - 20, 60), (x + 20, 60)),
        'b': ((x + 20, 60), (x + 20, 0)),
        'c': ((x + 20, 0), (x + 20, -60)),
        'd': ((x + 20, -60), (x - 20, -60)),
        'e': ((x - 20, -60), (x - 20, 0)),
        'f': ((x - 20, 0), (x - 20, 60)),
        'g': ((x - 15, 0), (x + 15, 0)),
    }

    # Сегменты для каждой цифры
    digits_segments = {
        '0': ['a', 'b', 'c', 'd', 'e', 'f'],
        '1': ['b', 'c'],
        '2': ['a', 'b', 'g', 'e', 'd'],
        '3': ['a', 'b', 'c', 'd', 'g'],
        '4': ['f', 'g', 'b', 'c'],
        '5': ['a', 'f', 'g', 'c', 'd'],
        '6': ['a', 'f', 'e', 'd', 'c', 'g'],
        '7': ['a', 'b', 'c'],
        '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        '9': ['a', 'b', 'c', 'd', 'f', 'g'],
    }

    turtle.pensize(8)
    turtle.color('black')

    if digit not in digits_segments:
        return
    
    for seg in digits_segments[digit]:
        start, end = segments_coords[seg]
        draw_segment(start, end)

number = input("Введите индекс: ")
turtle.speed(4)

start_x = -200
for i, digit in enumerate(number):
    if digit.isdigit():
        draw_digit(start_x + i * (DIGIT_WIDTH + GAP), digit)

turtle.hideturtle()
turtle.done()
'''
#газ

'''from random import *
import turtle

N_TURTLES = 10
STEPS = 500
BOX_WIDTH = 400
BOX_HEIGHT = 300
SPEED = 3

# Создает черепах
turtles_list = [turtle.Turtle(shape='turtle') for _ in range(N_TURTLES)]

for t in turtles_list:
    t.penup()
    t.speed(0)
    # Случайная начальная позиция
    t.goto(randint(-BOX_WIDTH//2+20, BOX_WIDTH//2-20),
           randint(-BOX_HEIGHT//2+20, BOX_HEIGHT//2-20))
    t.pendown()
    # Случайное направление движения
    t.setheading(randint(0, 360))

for step in range(STEPS):
    for t in turtles_list:
        # Движение
        t.forward(SPEED)
        
        # Отражение от стен
        if abs(t.xcor()) > BOX_WIDTH//2:
            t.right(90)  # отражение по нормали
        if abs(t.ycor()) > BOX_HEIGHT//2:
            t.right(90)
        
        # Простые столкновения
        for other in turtles_list:
            if t != other and t.distance(other) < 15:
                t.right(randint(-60, 60))
                other.right(randint(-60, 60))


turtle.speed(10)
for t in turtles_list:
    t.hideturtle()

# Рамка
t = turtle.Turtle()
t.speed(10)
t.pensize(3)
t.penup()
t.goto(-BOX_WIDTH//2, BOX_HEIGHT//2)
t.pendown()
for _ in range(2):
    t.forward(BOX_WIDTH)
    t.right(90)
    t.forward(BOX_HEIGHT)
    t.right(90)

turtle.done()
'''