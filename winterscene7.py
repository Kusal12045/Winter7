import turtle
import random


screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("lightsteelblue")

t_ground = turtle.Turtle()
t = turtle.Turtle()


t_ground.speed(100)
t.speed(100)

t_ground.penup()
t_ground.pencolor("snow1")
t_ground.fillcolor("snow1")
t_ground.begin_fill()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

t.pencolor("black")
t.fillcolor("snow1")
t.penup()
t.goto(0,-150)
t.pendown()
t.begin_fill()
t.circle(65)
t.end_fill()

t.speed(0)
t.penup()
t.goto(0,-65)
t.pendown()
t.begin_fill()
t.circle(55)
t.end_fill()

t.penup()
t.goto(0,25)
t.pendown()
t.begin_fill()
t.circle(45)
t.end_fill()

t.fillcolor("black")
t.penup()
t.goto(-20,65)
t.begin_fill()
t.circle(5)
t.end_fill()

t.fillcolor("black")
t.penup()
t.goto(20,65)
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.fillcolor("orange")
t.begin_fill()
t.goto(5,60)
t.goto(0,50)
t.goto(-5,60)
t.goto(5,60)
t.end_fill()
t.penup()

t.fillcolor("black")
t.goto(0,35)
t.begin_fill()
t.pendown()
t.circle(2.5)
t.end_fill()

t.penup()

t.goto(7,37)
t.begin_fill()
t.pendown()
t.circle(2.5)
t.end_fill()

t.penup()

t.goto(14,39)
t.begin_fill()
t.pendown()
t.circle(2.5)
t.end_fill()

t.penup()

t.goto(-7,37)
t.begin_fill()
t.pendown()
t.circle(2.5)
t.end_fill()

t.penup()

t.goto(-14,39)
t.begin_fill()
t.pendown()
t.circle(2.5)
t.end_fill()
t.penup()

t.goto(0,-100)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

t.goto(0,-50)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

t.goto(0,0)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()
t.penup()

t.pencolor("black")
t.fillcolor("darkorange4")
t.begin_fill()
t.goto(-50,15)
t.pendown()
t.goto(-100,-50)
t.goto(-90,-50)
t.goto(-50,0)
t.goto(-50,15)
t.end_fill()
t.penup()
t.goto(50,15)
t.begin_fill()
t.pendown()
t.goto(100,-50)
t.goto(90,-50)
t.goto(50,0)
t.goto(50,15)
t.end_fill()
t.penup()
t.goto(-300,300)
t.pendown()
t.pencolor("black")
t.fillcolor("cornsilk1")
t.pencolor("cornsilk1")

t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-200,275)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-100,250)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0,275)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(100,280)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(200,285)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(300,290)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.goto(100,-50)
t.pendown()
t.pensize(5)
t.setheading(90)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.setheading(90)
t.forward(5)
t.pencolor("white")
t.forward(5)
t.penup()
t.forward(15)
t.pendown()
t.forward(2.5)
t.penup()
t.setheading(-180)
t.forward(15)
t.pendown()
t.forward(5)
t.penup()
t.forward(5)
t.left(90)
t.forward(10)
t.pendown()
t.forward(5)
t.penup()
t.forward(10)
t.pendown()
t.forward(5)
t.penup()
t.forward(10)
t.pendown()
t.forward(5)
t.penup()
# that was candycane
t.goto(0,107)
t.pencolor("black")
t.fillcolor("black")
t.pendown()
t.setheading(0)
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(10)
t.left(90)
t.forward(15)
t.right(90)
t.forward(50)
t.left(90)
t.forward(65)
t.left(90)
t.forward(50)
t.right(90)
t.forward(15)
t.left(90)
t.forward(10)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()
t.goto(0,200)
t.write("Happy Holidays, Merry Christmas!", font=("Times New Roman", 24, "bold"), align = "center")

t.fillcolor("green")


t.goto(-200,0)
t.begin_fill()
t.pendown()
t.right(75)
t.forward(100)
t.setheading(180)
t.forward(75)
t.right(100)
t.forward(175)
t.right(156)
t.forward(80)
t.end_fill()
t.penup()
t.goto(-225,-100)
t.setheading(0)
t.right(90)
t.pensize(5)
t.fillcolor("darkorange4")
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.end_fill()


























# add stockings
# christmas tree
# present
# reindeer?
# santa?
# fireplace
# window with snowman visible
# table












# second page thing
enter = input("press enter to continue")
t.clear()
t_ground.clear()
screen.bgcolor("sienna1")

t_ground.penup()
t_ground.pencolor("saddlebrown")
t_ground.fillcolor("saddlebrown")
t_ground.begin_fill()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

















# this is the last line of code
turtle.done()