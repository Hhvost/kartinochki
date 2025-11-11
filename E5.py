from turtle import *

shape('turtle')
speed(10)
for i in range(1,11):
    for j in range(4):
        forward(20*i)
        left(90)
    penup()
    goto(-10*i,-10*i)
    pendown()
mainloop()