# S

'''import turtle

turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.done()
'''

#квадрат

'''import turtle

side = 100
for _ in range(4):
    turtle.forward(side)
    turtle.left(90)
turtle.done()
'''

#окружность

'''import turtle

radius = 100
sides = 360
angle = 360 / sides
for _ in range(sides):
    turtle.forward(radius * 0.1)
    turtle.right(angle)
turtle.done()
'''

#вложенные квадраты

'''import turtle

turtle.speed(5)

squares_coords = [
    [(-10, -10), (10, -10), (10, 10), (10, 10), (-10, 10), (-10, -10)],  # 20x20
    [(-20, -20), (20, -20), (20, 20), (20, 20), (-20, 20), (-20, -20)],  # 40x40
    [(-30, -30), (30, -30), (30, 30), (30, 30), (-30, 30), (-30, -30)],  # 60x60
    [(-40, -40), (40, -40), (40, 40), (40, 40), (-40, 40), (-40, -40)],  # 80x80
    [(-50, -50), (50, -50), (50, 50), (50, 50), (-50, 50), (-50, -50)],  # 100x100
    [(-60, -60), (60, -60), (60, 60), (60, 60), (-60, 60), (-60, -60)],  # 120x120
    [(-70, -70), (70, -70), (70, 70), (70, 70), (-70, 70), (-70, -70)],  # 140x140
    [(-80, -80), (80, -80), (80, 80), (80, 80), (-80, 80), (-80, -80)],  # 160x160
    [(-90, -90), (90, -90), (90, 90), (90, 90), (-90, 90), (-90, -90)],  # 180x180
    [(-100,-100), (100,-100),(100,100),(100,100),(-100,100),(-100,-100)]  # 200x200
]

for coords in squares_coords:
    turtle.penup()
    turtle.goto(coords[0])  
    turtle.setheading(0)
    turtle.pendown()
    
    for x, y in coords:
        turtle.goto(x, y)

turtle.done()
'''

#пружина

'''import turtle

turtle.speed(8)
turtle.penup()
turtle.goto(0, 0)
turtle.setheading(90) 
turtle.pendown()

for i in range(12):
    turtle.circle(30, 180)
    turtle.circle(-20, 180)

turtle.done()
'''

#звезды

import turtle

def star(n, size):
    angle = 180 - (180 / n)  
    for _ in range(n):
        turtle.forward(size)
        turtle.right(angle)

turtle.speed(5)
turtle.penup()
turtle.goto(-100, 50)
turtle.setheading(0)
turtle.pendown()
star(5, 80)  # 5-конечная

turtle.penup()
turtle.goto(100, -50)
turtle.setheading(0)
turtle.pendown()
star(11, 50)  # 11-конечная
turtle.done()
