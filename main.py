# Created by Ethan Ye with the help of Claude and Gemini specifically
# I swear I didn't use ChatGPT for this


import math
import time
import random
import sys
import pygame as pg

# settings as const vars

print("Hello World...")

CLOCK = pg.time.Clock()

pg.init()

WIDTH = 800
HEIGHT = 800

screen = pg.display.set_mode((WIDTH, HEIGHT))

playing = True

GREEN = (0, 255, 0)

# rectangle variables and the velocity
rectWidth  = 100
rectLength = 100

rectX= 350
rectY= 0



rectXVelocity = 0.1

rectVelocity = 5
rectAngle = 45

def screenSaverLoop():
    global rectX, rectY, rectVelocity, rectAngle
    bounce_counter = 0

    rectX += rectVelocity * math.cos(math.radians(rectAngle))
    rectY += rectVelocity * math.sin(math.radians(rectAngle))
    if rectX > WIDTH - rectWidth or rectX < 0:
        rectAngle = 180 - rectAngle
        bounce_counter += 1
        print(f"Rectangle position: ({rectX}, {rectY})")
    if rectY > HEIGHT - rectLength or rectY < 0:
        rectAngle = -rectAngle
        bounce_counter += 1
        print(f"Rectangle position: ({rectX}, {rectY})")

    rectAngle %= 360


class Game:
    def __init__(self):
        pass
    def input(self):
        pass
    
    def update(self):
        # global rectX, rectXVelocity
        # # update the position of the rectangle
        # rectX += rectXVelocity
        # # check for collision with screen edges
        # if rectX > WIDTH-100 or rectX < 0:
        #     rectXVelocity *= -1
        #     print("bounce")
        screenSaverLoop()
    
    def draw(self):
        screen.fill((100, 100, 100)) # red screen
        pg.draw.rect(screen, GREEN, (rectX, rectY, rectWidth, rectLength))
        pg.display.flip() # refreshes screen to show recent changes




            
            
if __name__ == "__main__":
    # create instance of game class/instantiating game class
    g = Game()
    # loop runs while playing is true
    while playing:
        g.draw()
        g.update()


        for event in pg.event.get():

            if event.type == pg.MOUSEBUTTONDOWN:
                print("input from mouse")

            if event.type == pg.QUIT:
                playing = False  # set playing to false to prevent next iteration of loop
            pg.display.flip()

        CLOCK.tick(120)