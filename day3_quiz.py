
'''
Create a pixel art character using the code below.

Things to think about:
Use of global variables
Use of color
Use of functions
Use of parameters
Use of arguments
Use of lists
Use of for loops

'''
MAP = ["xoooxxoxoxoooxooox",
       "xoooxxoxoxoooxooox",
       "xoooxxoxoxoooxooox"]

PIXEL_SIZE = 20

import turtle
import time
from turtle import *
from random import randint

turtle.colormode(255)

pen = turtle.Turtle()

pen.pensize(0)
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=640, height=640)

side_length = PIXEL_SIZE

def draw_pixel(x,y,color):
    pen.penup()

    pen.goto(x,y)

    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)             

    pen.end_fill()

start_time = time.time()

for y in range(32):
    for x in range(32):
        draw_pixel(-320+PIXEL_SIZE*x,320+PIXEL_SIZE*y*-1,"red")

end_time = time.time()

elapsed_time = end_time = start_time

print(elapsed_time)

turtle.done()      


# drawing a grid
for y in range(3):
    for x in range(3):
        print(f"y: {y}, x: {x}")



for i in MAP:
    print(i)
    for j in i:
        print(j)
        if j == "x":
            print("make it blue")