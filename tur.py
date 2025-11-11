import turtle

from math import sqrt

l = turtle.left
r = turtle.right
k = turtle.forward(20)
g = turtle.forward(20*sqrt(2))
u = turtle.penup
d = turtle.pendown
h = turtle.goto

a = list(input())
b = len(a)

for i in range(b):
    if a[i] == '0':
        ([h, (i*30, 0),  d, k, r, 90, k, k, r, 90, k, r, 90, k, k, u])
    if a[i] == '1':
        ([h, (i*30, -20), d, l, 45, g, r, 135, k, k, u])
    if a[i] == '2':
        ([h, (i*30, 0), d, k, r, 90, k, r, 90, k, l, 90, k, l, 90, k, u])
    if a[i] == '3':
        ([h, (i*30, 0), k, r, 135, g, l, 135, k, r, 135, g, u])

o = [h, (i*30, 0),  d, k, r, 90, k, k, r, 90, k, r, 90, k, k, u]
z = [h, (i*30, -20), d, l, 45, g, r, 135, k, k, u]
y = [h, (i*30, 0), d, k, r, 90, k, r, 90, k, l, 90, k, l, 90, k, u]
x = [h, (i*30, 0), k, r, 135, g, l, 135, k, r, 135, g, u]
        
        
import turtle

x = 0
y = 0
v = 2
d = 
t = 0
a = -9.8
for i in range(1000):
    x += vx*dt
    
    turtle.goto()
        

        

