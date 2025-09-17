import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
import math

class Player(Sprite):
    def __init__(self, game, x, y, speed):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pg.K_s] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed
        if keys[pg.K_d] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
    
    def update(self):
        self.get_keys()
    
        
    


class ScreenSaver(Sprite):
    def __init__(self, game, x, y, width, length, angle, velocity):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((width, length))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.velocity = velocity
    def update(self):
        self.rect.x += math.cos(math.radians(self.angle)) * self.velocity
        self.rect.y += math.sin(math.radians(self.angle)) * self.velocity
        if self.rect.x > WIDTH - self.rect.width or self.rect.x < 0:
            self.angle = 180 - self.angle
        if self.rect.y > HEIGHT - self.rect.height or self.rect.y < 0:
            self.angle = -self.angle
        self.angle %= 360