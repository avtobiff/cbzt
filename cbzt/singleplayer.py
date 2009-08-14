import pygame
import math
import random
import sys

import cbzt
from exception import EndGame
from game import Ball, Game
from player import AI, Player


class SinglePlayer(Game):
    def __init__(self,screen):
        pygame.key.set_repeat(1,50)
        self.area = screen.get_rect()
        self.ball = Ball((80,240))
        self.player = Player(40)
        self.ai = AI(600,self.ball)
        self.left, self.right = True, False # ball always starts on the left
        self.top, self.bottom = False, False
        Game.__init__(self,screen,self.player,self.ai,self.ball)


    def gameover(self):
        if self.ai.get_score() >= 9:
            msg = "YOU LOST"
        else:
            msg = "YOU WON"
        t = cbzt.text.render(msg,width=8,height=8)
        sw,sh = t.get_size()
        self.screen.blit(t,(320-sw/2,240-sh/2))
        pygame.display.flip()

        while 1:
            self.read_input(pygame.event.poll())


    def new_round(self):
        self.ball.reinit(self.left)
        self.player.reinit((40,240))
        self.ai.reinit((600,240))
        self.left, self.right = False, False

    def read_input(self,event):
        if event.type == pygame.QUIT:
            print "QUIT"
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise EndGame("EXIT SINGLE PLAYER")
            elif event.key == pygame.K_DOWN:
                self.p0.up()
            elif event.key == pygame.K_UP:
                self.p0.down()
