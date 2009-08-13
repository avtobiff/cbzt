import pygame
import cbzt
import cbzt.text


class Option(object):
    def __init__(self, state, name, active=False):
        self.state   = state
        self.name    = name.lower()
        if active:
            self.activate()
        else:
            self.deactivate()

    def get_state(self):
        return self.state

    def get_surface(self):
        return self.surface

    def activate(self):
        self.active = True
        self.surface = cbzt.text.render(self.name,fg=(255,0,0))

    def deactivate(self):
        self.active = False
        self.surface = cbzt.text.render(self.name)


class Textbox(object):
    pass


class Menu(object):
    def __init__(self,screen,options):
        self.screen = screen
        self.options = options
        self.background = pygame.Surface(screen.get_size())
        self.background.fill((0,)*3)

    def choose(self):
        # active menu option
        active = 0
        # TODO: make pertty
        while 1:
            # render menu options
            num = 0
            for option in self.options:
                s = option.get_surface()
                sw,sh = s.get_size()
                self.background.blit(s,(320-sw/2,240-(len(self.options)*40)/2-num*40))
                num -= 1

            self.screen.blit(self.background,(0,0))

            pygame.display.flip() # TODO: abstract out to a redraw method

            # read input and change menu accordingly
            self.options[active].deactivate()
            event = pygame.event.poll()
            # quit if QUIT event is catched
            if event.type == pygame.QUIT:
                return cbzt.QUIT
            # otherwise check if event should alter menu
            elif event.type == pygame.KEYDOWN:
                # return selected menu choice
                if event.key == pygame.K_RETURN:
                    return self.options[active].get_state()
                # move up in menu options
                elif event.key == pygame.K_UP:
                    if active is 0: active = len(self.options)-1
                    else:           active -= 1
                # move down in menu options
                elif event.key == pygame.K_DOWN:
                    if active is len(self.options)-1: active = 0
                    else:                             active += 1
            self.options[active].activate()




def launch(screen,options):
    print "RENDER MENU"
    menu = Menu(screen,options)
    return menu.choose()
