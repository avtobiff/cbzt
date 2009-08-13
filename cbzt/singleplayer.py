import pygame
import sys

import cbzt
from exception import EndGame
from game import Board, Game
from player import AI, Player


class SinglePlayer(Game):
    def __init__(self,screen):
        self.player = Player(40)
        self.ai = AI(600)
        Game.__init__(self,screen,self.player,self.ai)

    def game(self):
        while 1:
            for item in self.items:
                item.update()
                item.draw(self.screen)
                pygame.display.flip()

            # TODO: need collision detection

            self.read_input(pygame.event.poll())

    def read_input(self,event):
        if event.type == pygame.QUIT:
            print "QUIT"
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise EndGame("EXIT SINGLE PLAYER")
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_UP:
                pass
