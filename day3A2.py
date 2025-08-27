
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
PIXEL_SIZE = 20

PIXEL_ART_ARRAY = [
    #0-7
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "aquamarine", "aquamarine", "blue", "aquamarine", "aquamarine", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white"], #
    ["white", "white", "white", "white", "white", "white","white", "white", "white", "aquamarine", "aquamarine", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "brown", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "brown", "white", "white", "white", "white"], #
    ["aquamarine", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "white", "white", "white", "aquamarine", "blue", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "blue", "brown", "blue", "blue", "aquamarine", "aquamarine", "aquamarine", "brown", "brown", "brown", "white", "white", "white", "white", "white"], #
    ["brown", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "aquamarine", "blue", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "tan", "blue", "blue", "brown", "aquamarine", "aquamarine", "aquamarine", "brown", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["brown", "tan", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "blue", "tan", "tan", "tan", "blue", "brown", "aquamarine", "aquamarine", "brown", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["brown", "tan", "tan", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "tan", "tan", "blue", "blue", "brown", "brown", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["brown", "tan", "tan", "tan", "blue", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "blue", "blue", "blue", "aquamarine", "tan", "blue", "blue", "brown", "blue", "aquamarine", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["brown", "tan", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "white", "white", "white", "white", "white", "white", "white"],
    #8-15
    ["white", "white", "brown", "brown", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "brown", "white", "white","white","white"],
    ["white", "white","white", "brown", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "brown", "white", "white", "white", "cyan", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "brown", "white", "white", "white"],
    ["white", "white", "aquamarine", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "brown", "aquamarine", "white", "green", "white", "white", "cyan", "aquamarine", "blue", "blue", "blue", "blue", "aquamarine","aquamarine","aquamarine","aquamarine","aquamarine","aquamarine","aquamarine", "brown", "white", "white"],
    ["white", "white", "aquamarine", "blue", "aquamarine", "aquamarine", "blue", "blue", "blue", "blue", "brown", "white", "white", "green", "brown", "white", "white", "aquamarine", "blue", "blue", "blue", "aquamarine","aquamarine", "brown", "brown", "brown", "brown", "brown", "brown", "brown", "white", "white"],
    ["white", "white", "aquamarine", "blue", "aquamarine", "cyan", "aquamarine", "blue", "blue", "brown", "aquamarine", "white", "white", "green", "brown", "white", "white", "aquamarine", "blue", "blue", "aquamarine", "brown", "brown", "brown", "white", "white", "white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "brown", "brown", "cyan", "cyan", "brown", "blue", "brown", "white", "white", "white", "white", "brown", "white", "coral", "aquamarine", "aquamarine", "blue", "blue", "blue", "aquamarine", "brown", "brown", "white", "aquamarine", "aquamarine", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "brown", "white", "aquamarine", "brown", "brown", "brown", "white", "white", "white", "white", "white", "coral", "tan", "tan", "tan", "brown", "blue", "blue", "blue", "aquamarine", "aquamarine", "brown", "white", "white", "aquamarine", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "brown", "white", "aquamarine", "aquamarine", "brown", "white", "white", "white", "white", "white", "coral", "tan", "tan", "tan", "tan", "brown", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "brown", "white", "white", "white", "cyan", "cyan", "cyan", "cyan", "white", "white"],
    #16-23 red swapped to tan
    ["white", "white", "white", "white", "white", "brown", "brown", "brown", "orange", "orange", "orange", "orange", "orange", "tan", "tan", "orange", "orange", "tan", "tan", "brown", "aquamarine", "brown", "brown", "brown", "khaki", "khaki", "aquamarine", "aquamarine", "khaki", "khaki", "khaki", "aquamarine"], #
    ["white", "white", "white", "white", "white", "brown", "brown", "brown", "brown", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "coral", "brown", "aquamarine", "brown", "khaki", "khaki", "khaki", "khaki", "cyan", "cyan", "khaki", "khaki", "khaki", "khaki", "aquamarine"], #
    ["white", "white", "white", "white", "white", "white", "white", "white", "tan", "tan", "tan", "tan", "tan", "tan", "tan", "coral", "brown", "brown", "aquamarine", "aquamarine", "brown", "cyan", "cyan", "cyan", "cyan", "cyan", "cyan", "cyan", "cyan", "aquamarine", "aquamarine", "white"], #
    ["white", "white", "white", "white", "maroon", "maroon", "maroon", "maroon", "white", "white", "tan", "tan", "tan", "brown", "brown", "brown", "coral", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "brown", "brown", "brown", "cyan", "cyan", "gray", "gray", "cyan", "cyan", "cyan", "aquamarine"], #
    ["white", "white", "white", "aquamarine", "cyan", "khaki", "khaki", "firebrick", "maroon", "maroon", "white", "white", "white", "tan", "coral", "coral", "coral", "coral", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "brown", "brown", "cyan", "cyan", "cyan", "cyan", "gray", "gray", "cyan", "cyan", "aquamarine"], #
    ["white", "white", "white", "aquamarine", "aquamarine", "aquamarine", "aquamarine", "khaki", "firebrick", "firebrick", "maroon", "white", "white", "tan", "tan", "coral", "coral", "coral", "aquamarine", "aquamarine", "brown", "aquamarine", "aquamarine", "brown", "cyan", "cyan", "cyan", "gray", "brown", "brown", "brown", "white"], #
    ["white", "white", "white", "aquamarine", "gray", "gray", "gray", "aquamarine", "khaki", "cyan", "cyan", "maroon", "white", "tan", "orange", "tan", "tan", "coral", "aquamarine", "aquamarine", "brown", "brown", "brown", "brown", "brown", "brown", "brown", "brown", "white", "white", "white", "white"], #
    ["white", "white", "white", "aquamarine", "gray", "gray", "gray", "gray", "aquamarine", "khaki", "cyan", "cyan", "maroon", "white", "brown", "tan", "tan", "tan", "aquamarine", "blue", "blue", "brown", "brown", "khaki", "khaki", "aquamarine", "firebrick", "maroon", "white", "white", "white", "white"], #
 
]
import turtle
from turtle import *
from random import randint

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

for y in range(0, 23):
    for x in range(32):
        draw_pixel(-320+PIXEL_SIZE*x,320+PIXEL_SIZE*y*-1, PIXEL_ART_ARRAY[y][x])
        print("y: ", y, "x:", x)

turtle.done()      


# drawing a grid
for y in range(3):
    for x in range(3):
        print(f"y: {y}, x: {x}")