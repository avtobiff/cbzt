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
import cbzt.font


def head(list):
    return list[0]

def tail(list):
    return list[1:]

def draw_character(surface,s_xpos,char,dimension,bg,fg):
    width,height = dimension
    char_surface = pygame.Surface((cbzt.font.WIDTH*width,cbzt.font.HEIGHT*height))

    # return big block if character is not in font
    if char in cbzt.font.font:
        char_surface.fill(bg)
    else:
        char_surface.fill(fg)
        return char_surface

    char_pixel = pygame.Surface(dimension)
    char_pixel.fill(fg)
    ypos = 0

    for y in range(cbzt.font.HEIGHT):
        xpos = 0
        for x in range(cbzt.font.WIDTH):
            if cbzt.font.font[char][y][x]:
                char_surface.blit(char_pixel,(xpos,ypos))
            xpos += width
        ypos += height
    surface.blit(char_surface,(s_xpos,0))
    return surface

def render(string,bg=(0,)*3,fg=(255,)*3,width=5,height=5,surface=None,xpos=0):
    """
    string - the string to be rendered
    bg - background colour (default (0,0,0))
    fg - foreground colour (default (255,255,255))
    width - pixelwidth for each point in font (default = 5)
    height - pixelwidth for each point in font (default = 5)

    returns a surface with the rendered string
    """
    if len(string) <= 0: # return final product
        return surface
    elif surface is None: # create canvas
        # all character's widths plus spaces in between
        x = len(string)*width*(cbzt.font.WIDTH+1)
        # character height
        y = height*cbzt.font.HEIGHT
        s = pygame.Surface((x,y))
        s.fill(bg)
        return render(string.lower(),bg,fg,width,height,s)
    else: # recurse over string and draw message
        surface = draw_character(surface,xpos,head(string),(width,height),bg,fg)
        xpos += width*(cbzt.font.WIDTH+1) # space plus a new character
        return render(tail(string),bg,fg,width,height,surface,xpos)
