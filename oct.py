#Neva Buttrey (January 25, 2021 )
import turtle

neva=turtle.Turtle()
neva.color("red")
neva.speed(0)
x = -95
y = +95


for i in range(5):
    neva.penup()
    neva.goto(x,y)
    neva.pendown()
    #neva.begin_fill()
    for i in range(0,8):
        neva.fd(100)
        neva.right(45)
    #neva.end_fill()
    x +=  5
    y -=  5


neva.penup()
neva.goto(-75, +75)
neva.pendown()

neva.begin_fill()
for i in range(0,8):
    neva.fd(100)
    neva.right(45)
neva.end_fill()

neva.penup()
neva.goto(-75, -75)
neva.color("white")
neva.pendown()
neva.write("STOP",font = ("Impact", 40))
neva.hideturtle()



















