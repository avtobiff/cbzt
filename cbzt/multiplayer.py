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
            msg = "PLAYER 1 WON"
        else:
            msg = "PLAYER 2 WON"
        AbstractGame.over(msg)
