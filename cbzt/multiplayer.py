# -*- encoding: utf-8 -*-

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

import cbzt
from game import AbstractGame, Ball
from player import Player


class MultiPlayer(AbstractGame):
    def __init__(self,screen):
        self.mode = cbzt.MULTIPLAYER_LOCAL
        pygame.key.set_repeat(1,50)
        self.area = screen.get_rect()
        self.ball = Ball((80,240))
        self.playerone = Player(40)
        self.playertwo = Player(600)
        self.left, self.right = True, False # ball always starts on the left
        self.top, self.bottom = False, False
        AbstractGame.__init__(self,screen,self.playerone,self.playertwo,self.ball)

    def gameover(self):
        if self.p0.get_score() >= 9:
            msg = "PLAYER1 WON"
        else:
            msg = "PLAYER2 WON"
        AbstractGame.over(self,msg)
