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
        self.ball = Ball((80,240),random.random()*math.pi/2-random.random()*math.pi/2,5+random.random()*5)
        self.player = Player(40)
        self.ai = AI(600,self.ball)
        Game.__init__(self,screen,self.player,self.ai,self.ball)

    def game(self):
        while 1:
            for item in self.items:
                item.update()
                item.draw(self.screen)
                pygame.display.flip()

            # TODO: need collision detection

            self.read_input(pygame.event.poll())
            self.clock.tick(cbzt.FPS)

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
