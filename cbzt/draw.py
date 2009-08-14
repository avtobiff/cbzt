import pygame


class Drawable(pygame.sprite.Sprite):
    def __init__(self,surface,position):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = position
        surface.convert()
        self.image = surface
        self.rect = self.image.get_rect()

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def get_surface(self):
        return self.image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def position(self):
        return self.x, self.y

    def reinit(self,position):
        self.x, self.y = position
