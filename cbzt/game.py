import pygame
import math
import random

import cbzt
import pygame
from draw import Drawable
from exception import EndGame


class Ball(Drawable):
    def __init__(self,position):
        self.direction = 0
        self.velocity = 0
        ball = pygame.Surface((10,10))
        ball.fill((255,)*3)
        Drawable.__init__(self,ball,position)

    def draw(self,screen):
        self.rect = pygame.rect.Rect((self.x,self.y),(10,10))
        screen.blit(self.image,(self.x-5,self.y-5))

    def bounce(self,velocity=None,direction=None):
        if direction:
            self.direction = direction
        else:
            self.direction = -self.direction
        if velocity:
            self.velocity = velocity

    def reinit(self,left):
        if left:
            Drawable.reinit(self,(80,240))
            self.direction = random.random()*math.pi/2-math.pi/4
        else:
            Drawable.reinit(self,(540,240))
            self.direction = random.random()*math.pi+math.pi/4
        self.velocity = random.randint(5,10)

    def update(self):
        self.x += math.cos(self.direction)*self.velocity
        self.y += math.sin(self.direction)*self.velocity


class Board(Drawable):
    def __init__(self):
        self.build()
        Drawable.__init__(self,self.surface,(0,0))

    def build(self):
        self.surface= pygame.Surface((640,480))
        self.surface.fill((0,)*3)

        # middle markers
        marker = pygame.Surface((5,10))
        marker.fill((255,)*3)
        for y in range(32):
            self.surface.blit(marker,(320,y*20+5))


class Game(object):
    def __init__(self,screen,p0,p1,ball):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.board = Board()
        self.p0 = p0
        self.p1 = p1
        self.score0 = ScoreBoard(self.screen,250)
        self.score1 = ScoreBoard(self.screen,360)
        self.items = [self.board,self.p0,self.p1,self.ball,self.score0,self.score1]
        # start game
        self.game()

    def game(self):
        raise EndGame("EXIT GAME")


class ScoreBoard(Drawable):
    def __init__(self,screen,x):
        self.points = 0
        board = cbzt.text.render("0")
        Drawable.__init__(self,board,(x,20))

    def update(self):
        self.image = cbzt.text.render("%s" % self.points)

    def set_score(self,score):
        self.points = score
