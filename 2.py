# rt=right
# lt=left
# fd=forward
# bk=back=backward
# up=penup
# down=pendown
from turtle import *

p=int(input("Введите размер шрифта (число от 30 до 80, рекомендую 60) : "))
d=p*2**(1/2)

shape('turtle')
color("blue")
width(3)
speed(10)

up()
goto(-340,p*4)
down()

def zero():
    rt(90)
    fd(2*p)
    lt(90)
    fd(p)
    lt(90)
    fd(2*p)
    lt(90)
    fd(p)

def one():
    up()
    sety(ycor()-p)
    down()
    lt(45)
    fd(d)
    rt(135)
    fd(2*p)

def two():
    fd(p)
    rt(90)
    fd(p)
    rt(45)
    fd(d)
    lt(135)
    fd(p)

def tree():
    fd(p)
    rt(135)
    fd(d)
    lt(135)
    fd(p)
    rt(135)
    fd(d)

def four():
    rt(90)
    fd(p)
    lt(90)
    fd(p)
    rt(90)
    bk(p)
    fd(2*p)

def five():
    fd(p)
    bk(p)
    rt(90)
    fd(p)
    lt(90)
    fd(p)
    rt(90)
    fd(p)
    rt(90)
    fd(p)

def six():
    up()
    sety(ycor()-p)
    down()
    lt(45)
    fd(d)
    bk(d)
    rt(45)
    for j in 1,2,3,4:
        fd(p)
        rt(90)

def seven():
    fd(p)
    rt(135)
    fd(d)
    lt(45)
    fd(p)
    lt(90)

def eight():
    rt(90)
    fd(2*p)
    for j in 1,2,3:
        lt(90)
        fd(p)
    for j in 1,2,3:
        rt(90)
        fd(p)

def nine():
    for j in range(6):
        fd(p)
        rt(90)
    lt(90)
    fd(p)
    rt(90)
    fd(p)

def start(i):
    seth(0)
    up()
    goto(-340+1.5*p*i,p*4)
    down()

number=[zero,one,two,tree,four,five,six,seven,eight,nine]

post_ind=[1,4,1,7,0,0]
for i in range(6):
   number[post_ind[i]]()
   start(i+1)

up()
goto(-340,p)
down()

def start(i):
    seth(0)
    up()
    goto(-340+1.5*p*i,p)
    down()

post_ind=[int(i) for i in input("Введите почтовый индекс (набор из 6 цифр без пробелов): ")]

for i in range(len(post_ind)):
   number[post_ind[i]]()
   start(i+1)

mainloop()