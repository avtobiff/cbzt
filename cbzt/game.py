import pygame

import cbzt
from draw import Drawable
from exception import EndGame


class Board(Drawable):
    def __init__(self):
        self.build()
        Drawable.__init__(self,self.surface,0,0)

    def build(self):
        self.surface= pygame.Surface((640,480))
        self.surface.fill((0,)*3)

        # middle markers
        marker = pygame.Surface((5,10))
        marker.fill((255,)*3)
        for y in range(32):
            self.surface.blit(marker,(320,y*20))

class Game(object):
    def __init__(self,screen,p0,p1):
        self.screen = screen
        self.board = Board()
        self.p0 = p0
        self.p1 = p1
        self.items = [self.board,self.p0,self.p1]
        # start game
        self.game()

    def game(self):
        raise EndGame("EXIT GAME")
