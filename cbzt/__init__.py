import sys
import pygame
import menu
import singleplayer

from exception import EndGame


# enumaretion of states
QUIT, MENU, SINGLEPLAYER, MULTIPLAYER, HOST, CONNECT = range(6)

# draw this many frames per second
FPS = 20


class CBZT(object):
    def __init__(self):
        print "INITIALIZING"
        self.state = MENU
        pygame.display.init()
        pygame.display.set_caption("CBZT")
        pygame.key.set_repeat(500,100)
        self.screen = pygame.display.set_mode((640,480))
        self.screen.fill((0,)*3)

    def mainloop(self):
        print "MAIN LOOP"
        # satan machine for game
        while self.state is not QUIT:
            if self.state == MENU:
                print "MAIN MENU"
                options = [menu.Item("CBZT"),
                           menu.Option(SINGLEPLAYER,"SINGLE PLAYER",True),
                           menu.Option(MULTIPLAYER,"MULTIPLAYER"),
                           menu.Option(QUIT,"QUIT")]
                self.state = menu.launch(self.screen,options)
            elif self.state == SINGLEPLAYER:
                print "SINGLE PLAYER GAME"
                try:
                    singleplayer.SinglePlayer(self.screen)
                except EndGame, e:
                    print e.msg
                    self.state = MENU
            elif self.state == MULTIPLAYER:
                print "MULTIPLAYER MENU"
                options = [menu.Item("MULTIPLAYER"),
                           menu.Option(MENU,"NOT IMPLEMENTED",True),]
                           #menu.Option(HOST,"HOST",True),
                           #menu.Option(CONNECT,"CONNECT"),
                           #menu.Option(MENU,"MAIN MENU")]
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
