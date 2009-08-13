import pygame
import cbzt.font


def head(list):
    return list[0]

def tail(list):
    return list[1:]

def draw_character(surface,s_xpos,char,dimension,bg,fg):
    width,height = dimension
    char_surface = pygame.Surface((cbzt.font.WIDTH*width,cbzt.font.HEIGHT*height))
    char_surface.fill(bg)
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
        return render(string,bg,fg,width,height,s)
    else: # recurse over string and draw message
        surface = draw_character(surface,xpos,head(string),(width,height),bg,fg)
        xpos += width*(cbzt.font.WIDTH+1) # space plus a new character
        return render(tail(string),bg,fg,width,height,surface,xpos)
