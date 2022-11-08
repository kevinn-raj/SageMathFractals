from turtle import Turtle
from turtle import Screen
import turtle
import numpy as np


turtle.bye()
t = Turtle()

turtle.screensize(1500, 1500)
t.pensize(.1)

iterations = 5
angle = np.pi / 3

d = t.screen.window_width()/(3**iterations)/2

axiom = "F--F--F"
pathStr = axiom
ruleF = "F+F--F+F"

# for i in range(iterations):
#     temp = ""
#     for s in pathStr:
#         temp.replace_lttr(s)



t.speed(0);turtle.delay(0)
t.penup()
t.setpos(-t.screen.window_width()/4,0)
t.pendown()
t.radians()

for i in range(iterations):
    pathStr = pathStr.replace("F", ruleF)

for s in pathStr:
    s = s.upper()
    if s == "F" :
        t.fd(d)
    elif s == "+":
        t.left(angle)
        # t.fd(d)
    elif s == "-":
        t.right(angle)
        # t.rt()  

t.getscreen().getcanvas().postscript(file="NiceHexSpiral.eps")
turtle.exitonclick()