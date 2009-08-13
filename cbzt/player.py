import pygame

from draw import Drawable


class Player(Drawable):
    def __init__(self,x,name=""):
        paddle = pygame.Surface((10,30))
        paddle.fill((255,)*3)
        Drawable.__init__(self,paddle,x,240)
        self.name = name
        self.score = 0

    def up(self):
        self.y += 5

    def down(self):
        self.y -= 5

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def score(self):
        self.score += 1

    def update(self):
        pass


class AI(Player):
    def think(self, ball):
        if ball.get_y() < self.get_y():
            self.down()
        else:
            self.up()
