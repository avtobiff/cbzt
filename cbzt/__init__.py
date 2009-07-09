import sys
import pygame
import menu


# enumaretion of states
QUIT, MENU, MULTIPLAYER, HOST, CONNECT = range(5)

class CBZT(object):


    def __init__(self):
        print "INITIALIZING"
        self.state = MENU
        pygame.display.init()
        self.screen = pygame.display.set_mode((640,480))

    def mainloop(self):
        print "MAIN LOOP"
        # satan machine for game
        while self.state is not QUIT:
            if self.state == MENU:
                print "MAIN MENU"
                options = [menu.Option(MULTIPLAYER,"MULTIPLAYER",True),
                           menu.Option(QUIT,"QUIT")]
                self.state = menu.launch(self.screen,options)
            elif self.state == MULTIPLAYER:
                print "MULTIPLAYER MENU"
                options = [menu.Option(HOST,"HOST",True),
                           menu.Option(CONNECT,"CONNECT"),
                           menu.Option(MENU,"MAIN MENU")]
                self.state = menu.launch(self.screen,options)
            elif self.state == HOST:
                print "HOST GAME"
                options = [menu.Option(MULTIPLAYER,"BACK")]
                self.state = menu.launch(self.screen,options)
            elif self.state == CONNECT:
                print "CONNECT TO GAME"
                options = [menu.Option(MULTIPLAYER,"BACK")]
                self.state = menu.launch(self.screen,options)


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
