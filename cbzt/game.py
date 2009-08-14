# This file is part of CBZT.
#
# CBZT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CBZT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CBZT.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright © Per Andersson 2009

import pygame
import math
import random
import sys

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


class AbstractGame(object):
    def __init__(self,screen,p0,p1,ball):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.board = Board()
        self.hit = False
        self.p0 = p0
        self.p1 = p1
        self.score0 = ScoreBoard(self.screen,250)
        self.score1 = ScoreBoard(self.screen,360)
        self.items = [self.board,self.p0,self.p1,self.ball,self.score0,self.score1]
        # start game
        self.new_round()
        self.loop()

    def collision(self):
        self.hit = False
        if not self.area.contains(self.ball.rect):
            self.left   = self.ball.get_x() < 5
            self.right  = self.ball.get_x() > 635
            self.top    = self.ball.get_y() < 5
            self.bottom = self.ball.get_y() > 475
        else: # collide with players
            self.p0.rect.inflate(-9,0)
            self.p1.rect.inflate(-9,0)

            if self.ball.rect.colliderect(self.p0.rect) and not self.hit:
                self.hit = True
                x = self.p0.get_x()-self.ball.get_x()
                y = self.p0.get_y()-self.ball.get_y()
                velocity = math.sqrt(x**2+y**2)
                direction = math.atan2(x,y)
                self.ball.bounce(velocity,direction)
            elif self.ball.rect.colliderect(self.p1.rect) and not self.hit:
                self.hit = True
                x = self.p1.get_x()-self.ball.get_x()
                y = self.p1.get_y()-self.ball.get_y()
                velocity = math.sqrt(x**2+y**2)
                direction = math.atan2(x,y)
                self.ball.bounce(velocity,direction)
            elif self.hit:
                self.hit = False

    def loop(self):
        while 1:
            for item in self.items:
                item.update()
                item.draw(self.screen)
                pygame.display.flip()

            if self.p0.get_score() >= 9 or self.p1.get_score() >= 9:
                break

            self.collision()

            if self.left:
                self.p1.do_score()
                self.score1.set_score(self.p1.get_score())
                self.new_round()
                self.right = False
            elif self.right:
                self.p0.do_score()
                self.score0.set_score(self.p0.get_score())
                self.new_round()
                self.right = False
            elif self.top or self.bottom:
                self.ball.bounce()
                self.top, self.bottom = False, False

            self.read_input(pygame.event.poll())
            self.clock.tick(cbzt.FPS)

        self.gameover()

    def new_round(self):
        self.ball.reinit(self.left)
        self.p0.reinit((40,240))
        self.p1.reinit((600,240))
        self.left, self.right = False, False

    def over(self,msg):
        t = cbzt.text.render(msg,width=8,height=8)
        sw,sh = t.get_size()
        self.screen.blit(t,(320-sw/2,240-sh/2))
        pygame.display.flip()

        while 1:
            self.read_input(pygame.event.poll())

    def read_input(self,event):
        if event.type == pygame.QUIT:
            print "QUIT"
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise EndGame("EXIT SINGLE PLAYER")
            if event.key == pygame.K_s:
                self.p0.up()
            elif event.key == pygame.K_w:
                self.p0.down()
            elif event.key == pygame.K_DOWN and self.mode == cbzt.MULTIPLAYER_LOCAL:
                self.p1.up()
            elif event.key == pygame.K_UP and self.mode == cbzt.MULTIPLAYER_LOCAL:
                self.p1.down()


class ScoreBoard(Drawable):
    def __init__(self,screen,x):
        self.points = 0
        board = cbzt.text.render("0")
        Drawable.__init__(self,board,(x,20))

    def update(self):
        self.image = cbzt.text.render("%s" % self.points)

    def set_score(self,score):
        self.points = score
