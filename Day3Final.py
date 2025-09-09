# Ethan Ye, James Li, Matthew Sheyda, Brendon Pham

from turtle import Screen, Turtle, done
from time import time

PIXEL_SIZE = 20

PIXEL_ART_ARRAY = [
    #0-7
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "darkslategray", "darkslategray", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "white", "white", "white", "white", "white", "white"], #
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "white", "white"], #
    ["darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "white", "white", "white", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "black", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "black", "black", "black", "white", "white", "white", "white", "white"], #
    ["black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "navajowhite", "darkcyan", "darkcyan", "black", "darkslategray", "darkslategray", "darkslategray", "black", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "navajowhite", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "navajowhite", "navajowhite", "navajowhite", "darkcyan", "black", "darkslategray", "darkslategray", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "navajowhite", "navajowhite", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "navajowhite", "navajowhite", "darkcyan", "darkcyan", "black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "navajowhite", "navajowhite", "navajowhite", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "navajowhite", "darkcyan", "darkcyan", "black", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "white", "white", "white", "white", "white", "white", "white", "white", "white"], #
    ["black", "navajowhite", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "white", "white", "white", "white", "white", "white", "white"],
    #8-15
    ["white", "white", "black", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "white", "white"],
    ["white", "white", "white", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "white", "powderblue", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "black", "white", "white", "white"],
    ["white", "white", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "darkslategray", "white", "green", "white", "white", "powderblue", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "black", "white", "white"],
    ["white", "white", "darkslategray", "darkcyan", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "black", "white", "white", "green", "black", "white", "white", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
    ["white", "white", "darkslategray", "darkcyan", "darkslategray", "powderblue", "darkslategray", "darkcyan", "darkcyan", "black", "darkslategray", "white", "white", "green", "black", "white", "white", "darkslategray", "darkcyan", "darkcyan", "darkslategray", "black", "black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "black", "black", "powderblue", "powderblue", "black", "darkcyan", "black", "white", "white", "white", "white", "black", "white", "sandybrown", "darkslategray", "darkslategray", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "black", "black", "white", "darkslategray", "darkslategray", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "black", "white", "darkslategray", "black", "black", "black", "white", "white", "white", "white", "white", "sandybrown", "navajowhite", "navajowhite", "navajowhite", "black", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "black", "white", "white", "darkslategray", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "black", "white", "darkslategray", "darkslategray", "black", "white", "white", "white", "white", "white", "sandybrown", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "black", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "black", "white", "white", "white", "powderblue", "powderblue", "powderblue", "powderblue", "white", "white"],
    #16-23
    ["white", "white", "white", "white", "white", "black", "black", "black", "sandybrown", "sandybrown", "sandybrown", "sandybrown", "sandybrown", "navajowhite", "navajowhite", "sandybrown", "sandybrown", "navajowhite", "navajowhite", "black", "darkslategray", "black", "black", "black", "azure", "azure", "darkslategray", "darkslategray", "azure", "azure", "azure", "darkslategray"], #
    ["white", "white", "white", "white", "white", "black", "black", "black", "black", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "sandybrown", "black", "darkslategray", "black", "azure", "azure", "azure", "azure", "powderblue", "powderblue", "azure", "azure", "azure", "azure", "darkslategray"], #
    ["white", "white", "white", "white", "white", "white", "white", "white", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "navajowhite", "sandybrown", "black", "black", "darkslategray", "darkslategray", "black", "powderblue", "powderblue", "powderblue", "powderblue", "powderblue", "powderblue", "powderblue", "powderblue", "darkslategray", "darkslategray", "white"], #
    ["white", "white", "white", "white", "maroon", "maroon", "maroon", "maroon", "white", "white", "navajowhite", "navajowhite", "navajowhite", "black", "black", "black", "sandybrown", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "black", "black", "black", "powderblue", "powderblue", "cadetblue", "cadetblue", "powderblue", "powderblue", "powderblue", "darkslategray"], #
    ["white", "white", "white", "darkslategray", "powderblue", "azure", "azure", "firebrick", "maroon", "maroon", "white", "white", "white", "navajowhite", "sandybrown", "sandybrown", "sandybrown", "sandybrown", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "black", "black", "powderblue", "powderblue", "powderblue", "powderblue", "cadetblue", "cadetblue", "powderblue", "powderblue", "darkslategray"], #
    ["white", "white", "white", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "azure", "firebrick", "firebrick", "maroon", "white", "white", "navajowhite", "navajowhite", "sandybrown", "sandybrown", "sandybrown", "darkslategray", "darkslategray", "black", "darkslategray", "darkslategray", "black", "powderblue", "powderblue", "powderblue", "cadetblue", "black", "black", "black", "white"], #
    ["white", "white", "white", "darkslategray", "gray", "gray", "gray", "darkslategray", "azure", "powderblue", "powderblue", "maroon", "white", "navajowhite", "sandybrown", "navajowhite", "navajowhite", "sandybrown", "darkslategray", "darkslategray", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "white", "white"], #
    ["white", "white", "white", "darkslategray", "gray", "gray", "gray", "gray", "darkslategray", "azure", "powderblue", "powderblue", "maroon", "white", "black", "navajowhite", "navajowhite", "navajowhite", "darkslategray", "darkcyan", "darkcyan", "black", "black", "azure", "azure", "darkslategray", "firebrick", "maroon", "white", "white", "white", "white"], #
    #24-33
    ["white", "white", "white", "darkslategray", "gray", "gray", "gray", "darkslategray", "gray", "darkslategray", "white", "gray", "red", "maroon", "black", "black", "sandybrown", "navajowhite", "black", "darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkslategray", "white", "white", "darkslategray", "red", "maroon", "white", "white", "white"], #
    ["white", "white", "white", "white", "black", "gray", "darkslategray", "gray", "gray", "darkslategray", "white", "red", "red", "maroon", "darkslategray", "darkslategray", "black", "black", "black", "black", "darkcyan", "darkcyan", "darkslategray", "darkslategray", "white", "powderblue", "darkslategray", "white", "maroon", "white", "white", "white"], #
    ["white", "white", "white", "white", "black", "darkslategray", "gray", "gray", "darkslategray", "darkslategray", "darkslategray", "gray", "red", "red", "black", "darkslategray", "black", "white", "white", "white", "black", "black", "black", "black", "powderblue", "powderblue", "darkslategray", "white", "white", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "black", "gray", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "powderblue", "red", "red", "black", "black", "white", "white", "white", "white", "white", "white", "white", "black", "black", "darkslategray", "white", "white", "white", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "white", "black", "darkslategray", "darkslategray", "darkslategray", "darkslategray", "powderblue", "red", "red", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white", "red", "red", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "white", "white", "black", "darkslategray", "darkslategray", "darkslategray", "powderblue", "red", "black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "red", "red", "red", "maroon", "white", "white"], #
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white",],
    ["white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white",]
]
 
 


# set up pen
pen = Turtle()
pen.pensize(0)
pen.speed(0)
pen.hideturtle()

# initialize screen
screen = Screen()

# set screen backgrond color
screen.bgcolor("light blue")

# set screen size
screen.setup(width=640, height=640)

# performance, disable animation
screen.tracer(0, 0)

side_length = PIXEL_SIZE


# draw pixel function
def draw_pixel(x,y,color):
    pen.penup()

    pen.goto(x,y)

    pen.pendown()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)             

    pen.end_fill()


def main():
    # main loop
    start = time()
    for y in range(0, 30):
        for x in range(32):
            draw_pixel(-320+PIXEL_SIZE*x, # start from negative x and add side length every iteration
                    320+PIXEL_SIZE*y*-1, # start from positive y and subtract side length every iteration
                    PIXEL_ART_ARRAY[y][x]) # use y, x because the pixel array contains lists (y-axis) then elements(x-axis)
                                            # unfortunate effect of a readable 2d array, because the computer reads first the row (y) then the element(x)
            #print("y: ", y, "x:", x)
    end = time()
    print(f"Total time elapsed: {end-start} seconds")
    screen.update()
    done()
    return 0
    

if __name__ == "__main__":
    main()
