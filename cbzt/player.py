import pygame

from draw import Drawable


# constants
# change in y axis
DY = 5
TOP = 40
BOTTOM = 440


class Player(Drawable):
    def __init__(self,x,name=""):
        paddle = pygame.Surface((10,30))
        paddle.fill((255,)*3)
        Drawable.__init__(self,paddle,x,240)
        self.name = name
        self.score = 0

    def draw(self,screen):
        screen.blit(self.surface,(self.x-5,self.y-15))

    def up(self):
        if self.y < BOTTOM:
            self.y += DY

    def down(self):
        if self.y > TOP:
            self.y -= DY

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
    def __init__(self,x,ball):
        Player.__init__(self,x,"HAL")
        self.ball = ball

    def update(self):
        if self.ball.get_y() < self.get_y():
            self.down()
        else:
            self.up()
