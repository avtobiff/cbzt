import pygame
import sys

import cbzt
from exception import EndGame
from game import Board, Game


class SinglePlayer(Game):
    def __init__(self,screen):
        Game.__init__(self,screen)

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
            raise EndGame("EXIT SINGLE PLAYER")
