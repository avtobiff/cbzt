# -*- encoding: utf-8 -*-

# This file is part of CBZT.
#
# CBZT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CBZT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CBZT.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright © Per Andersson 2009

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
