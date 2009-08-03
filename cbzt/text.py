import pygame
import cbzt.font


def head(list):
    return list[0]

def tail(list):
    return list[1:]

def draw_character(surface,xpos,char,dimension,bg,fg):
    width,height = dimension
    char_surface = pygame.Surface((cbzt.font.WIDTH*width,cbzt.font.HEIGHT*height))
    char_surface.fill(bg)
    char_pixel = pygame.Surface(dimension)
    char_pixel.fill(fg)
    ypos = 0
    for y in range(cbzt.font.HEIGHT):
        ypos += height
        xpos = 0
        for x in range(cbzt.font.WIDTH):
            xpos += width
            if cbzt.font.font[char][x][y]:
                char_surface.blit(char_pixel,(xpos,ypos))
    print "drawc",char
    return char_surface

def draw(string,bg=(0,)*3,fg=(255,)*3,width=5,height=5,surface=None,xpos=0):
    """
    string - the string to be rendered
    bg - background colour (default (0,0,0))
    fg - foreground colour (default (255,255,255))
    width - pixelwidth for each point in font (default = 5)
    height - pixelwidth for each point in font (default = 5)

    returns a surface with the rendered string
    """
    if len(string) <= 0:
        return surface
    elif surface is None:
        # all character's widths plus spaces in between
        x = len(string)*width*cbzt.font.WIDTH+(len(string)-1)*cbzt.font.WIDTH
        # character height
        y = cbzt.font.HEIGHT
        s = pygame.Surface((x,y))
        s.fill(bg)
        return draw(string,bg,fg,width,height,s)
    else:
        xpos += cbzt.font.WIDTH+1 # space plus a new character
        draw_character(surface,xpos,head(string),(width,height),bg,fg)
        return draw(tail(string),bg,fg,width,height,surface,xpos)
