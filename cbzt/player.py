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

import random

import pygame

from draw import Drawable


# constants
# change in y axis
DY = 5
TOP = 40
BOTTOM = 440


class Player(Drawable):
    def __init__(self,x,name=""):
        paddle = pygame.Surface((10,30))
        paddle.fill((255,)*3)
        Drawable.__init__(self,paddle,(x,240))
        self.name = name
        self.score = 0

    def draw(self,screen):
        self.rect = pygame.rect.Rect((self.x,self.y),(10,30))
        screen.blit(self.image,(self.x-5,self.y-15))

    def up(self):
        if self.y < BOTTOM:
            self.y += DY

    def down(self):
        if self.y > TOP:
            self.y -= DY

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def do_score(self):
        self.score += 1


class AI(Player):
    def __init__(self,x,ball):
        Player.__init__(self,x,"HAL")
        self.ball = ball

    def update(self):
        if random.random() > 0.4:
            if self.ball.get_y() < self.get_y():
                self.down()
            else:
                self.up()
