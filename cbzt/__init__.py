import sys
import pygame
import menu


# enumaretion of states
QUIT, MENU, SINGLEPLAYER, MULTIPLAYER, HOST, CONNECT = range(6)

class CBZT(object):
    def __init__(self):
        print "INITIALIZING"
        self.state = MENU
        pygame.display.init()
        pygame.display.set_caption("CBZT")
        self.screen = pygame.display.set_mode((640,480))
        self.screen.fill((0,)*3)

    def mainloop(self):
        print "MAIN LOOP"
        # satan machine for game
        while self.state is not QUIT:
            if self.state == MENU:
                print "MAIN MENU"
                options = [menu.Option(SINGLEPLAYER,"SINGLE PLAYER",True),
                           menu.Option(MULTIPLAYER,"MULTIPLAYER"),
                           menu.Option(QUIT,"QUIT")]
                self.state = menu.launch(self.screen,options)
            elif self.state == SINGLEPLAYER:
                print "SINGLE PLAYER GAME"
                # TODO: launch single player game
            elif self.state == MULTIPLAYER:
                print "MULTIPLAYER MENU"
                options = [menu.Option(MULTIPLAYER,"NOT IMPLEMENTED",True),
                           #menu.Option(HOST,"HOST",True),
                           #menu.Option(CONNECT,"CONNECT"),
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
    except Exception, e:
        print >>sys.stderr,"ERROR"
        print >>sys.stderr,e
        return 1
    print "QUIT"
    return 0
