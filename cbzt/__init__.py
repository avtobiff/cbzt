import sys
import pygame
import menu


# enumaretion of states
QUIT, MENU, MULTIPLAYER = range(3)

class CBZT(object):


    def __init__(self):
        print "INITIALIZING"
        self.state = MENU
        pygame.display.init()
        self.screen = pygame.display.set_mode((640,480))

    def mainloop(self):
        print "MAIN LOOP"
        while self.state is not QUIT:
            if self.state == MENU:
                self.state = menu.launch(self.screen)
            elif self.state == MULTIPLAYER:
                pass


def launch():
    print "LAUNCHING CBZT"
    try:
        cbzt = CBZT()
        cbzt.mainloop()
    except:
        print >>sys.stderr,"ERROR"
        return 1
    print "QUIT"
    return 0
