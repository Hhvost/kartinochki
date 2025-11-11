from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 1000

turtle.tracer(False)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.setheading(randint(0, 360))
    unit.goto(randint(-100, 100), randint(-100, 100))
    

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(1)
    if unit.xcor() > 200:
        unit.setheading(180-unit.heading())
    if unit.ycor() > 200:
        unit.setheading(-unit.heading())
    if unit.xcor() < -200:
        unit.setheading(180-unit.heading())
    if unit.ycor() < -200:
        unit.setheading(-unit.heading())
    turtle.update()
turtle.update()
