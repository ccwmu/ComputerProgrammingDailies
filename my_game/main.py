# Created by Ethan Ye with the help of Claude and Gemini specifically
# I swear I didn't use ChatGPT for this...

import math
import time
import random
import sys
import pygame as pg

from settings import *
from sprites import *

# rectangle variables and the velocity
rectWidth  = 100
rectLength = 100
rectX= 350
rectY= 0
rectVelocity = 2
rectAngle = 45

#player variables
playerX = 50
playerY = 50
playerSpeed = 2

class Game:
    
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Ethan Ye's amazing breathtaking captivating dazzling exceptional fantastic glorious heroic incredible jaw-dropping knockout legendary marvelous noteworthy outstanding phenomenal quality remarkable stunning tremendous unbelievable visionary wonderful xceptional youthful zestful game")
        self.playing = True


    def new(self):
        # sprite Group to update, draw sprites in batches
        self.all_sprites = pg.sprite.Group()
        self.mob1 = ScreenSaver(self, rectX, rectY, rectWidth, rectLength, rectAngle, rectVelocity)
        self.player = Player(self, playerX, playerY, playerSpeed)
        self.all_sprites.add(self.mob1)
        self.all_sprites.add(self.player)
        # self.player = Player(self, 100, 100)
        # self.mob = Mob(self, 100, 100)
        # self.all_sprites.add(self.player)
        # self.all_sprites.add(self.mob)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    print("ts is happening")
                    self.playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                print("input from mouse")

    def update(self):
        self.all_sprites.update()
        #collisions
        
        if pg.sprite.collide_rect(self.player, self.mob1):
            print("Collision")
        pg.display.flip()


    def draw(self):
        self.screen.fill(LIGHT_GRAY) # white screen
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        # screen.fill((100, 100, 100)) # red screen
        #
        # pg.display.flip() # refreshes screen to show recent changes




            
            
if __name__ == "__main__":
    # create instance of game class/instantiating game class
    g = Game()
    g.new()
    # loop runs while playing is true
    g.run()
