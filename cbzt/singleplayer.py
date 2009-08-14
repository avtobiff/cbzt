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

    def collision(self):
        hit = False
        if not self.area.contains(self.ball.rect):
            self.left   = self.ball.get_x() < 5
            self.right  = self.ball.get_x() > 635
            self.top    = self.ball.get_y() < 5
            self.bottom = self.ball.get_y() > 475


        else: # collide with players
            self.player.rect.inflate(-9,0)
            self.ai.rect.inflate(-9,0)

            if self.ball.rect.colliderect(self.player.rect) and not hit:
                hit = True
                x = self.player.get_x()-self.ball.get_x()
                y = self.player.get_y()-self.ball.get_y()
                velocity = math.sqrt(x**2+y**2)
                direction = math.atan2(x,y)
                self.ball.bounce(velocity,direction)
            elif self.ball.rect.colliderect(self.ai.rect) and not hit:
                hit = True
                x = self.ai.get_x()-self.ball.get_x()
                y = self.ai.get_y()-self.ball.get_y()
                velocity = math.sqrt(x**2+y**2)
                direction = math.atan2(x,y)
                self.ball.bounce(velocity,direction)
            elif hit:
                self.hit = False


    def game(self):
        while 1:
            for item in self.items:
                item.update()
                item.draw(self.screen)
                pygame.display.flip()

            if self.ai.get_score() >= 9 or self.player.get_score() >= 9:
                break

            self.collision()

            if self.left:
                self.ai.do_score()
                self.score1.set_score(self.ai.get_score())
                self.new_round()
                self.right = False
            elif self.right:
                self.player.do_score()
                self.score0.set_score(self.player.get_score())
                self.new_round()
                self.right = False
            elif self.top or self.bottom:
                self.ball.bounce()
                self.top, self.bottom = False, False

            self.read_input(pygame.event.poll())
            self.clock.tick(cbzt.FPS)

        return self.gameover()

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
