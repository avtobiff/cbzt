class Drawable(object):
    def __init__(self,surface,x,y):
        self.x = x
        self.y = y
        self.surface = surface

    def draw(self,screen):
        screen.blit(self.surface,(self.x,self.y))

    def get_surface(self):
        return self.surface

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        pass
