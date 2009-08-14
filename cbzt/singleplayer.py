import pygame

import cbzt
from game import Ball, Game
from player import AI, Player


class SinglePlayer(Game):
    def __init__(self,screen):
        self.mode = cbzt.SINGLEPLAYER
        pygame.key.set_repeat(1,50)
        self.area = screen.get_rect()
        self.ball = Ball((80,240))
        self.player = Player(40)
        self.ai = AI(600,self.ball)
        self.left, self.right = True, False # ball always starts on the left
        self.top, self.bottom = False, False
        Game.__init__(self,screen,self.player,self.ai,self.ball)

    def gameover(self):
        if self.p1.get_score() >= 9:
            msg = "YOU LOST"
        else:
            msg = "YOU WON"
        Game.over(msg)
