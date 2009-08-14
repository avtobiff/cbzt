import pygame
import cbzt.text


class Item(object):
    def __init__(self, name):
        self.name    = name
        self.surface = cbzt.text.render(self.name,fg=(255,255,0))

    def get_surface(self):
        return self.surface

    def selectable(self):
        return False


class Option(Item):
    def __init__(self, state, name, active=False):
        Item.__init__(self,name)
        self.state   = state
        if active:
            self.activate()
        else:
            self.deactivate()

    def activate(self):
        self.active = True
        self.surface = cbzt.text.render(self.name,fg=(255,0,0))

    def deactivate(self):
        self.active = False
        self.surface = cbzt.text.render(self.name)

    def get_state(self):
        return self.state

    def selectable(self):
        return True


class Textbox(object):
    pass


class Menu(object):
    def __init__(self,screen,items):
        self.screen = screen
        self.items = items
        self.background = pygame.Surface(screen.get_size())
        self.background.fill((0,)*3)
        pygame.key.set_repeat(500,100)

    def choose(self):
        # active menu option
        active = 0
        # check which items are options
        selectable = [i for (i,o) in zip(range(len(self.items)),self.items) if o.selectable()]
        # TODO: make pertty
        while 1:
            # render menu items
            num = 0
            for option in self.items:
                s = option.get_surface()
                sw,sh = s.get_size()
                self.background.blit(s,(320-sw/2,240-(len(self.items)*40)/2-num*40))
                num -= 1

            self.screen.blit(self.background,(0,0))

            pygame.display.flip() # TODO: abstract out to a redraw method

            # read input and change menu accordingly
            self.items[selectable[active]].deactivate()
            event = pygame.event.poll()
            # quit if QUIT event is catched
            if event.type == pygame.QUIT:
                return cbzt.QUIT
            # otherwise check if event should alter menu
            elif event.type == pygame.KEYDOWN:
                # return selected menu choice
                if event.key == pygame.K_RETURN:
                    return self.items[selectable[active]].get_state()
                # move up in menu options
                elif event.key == pygame.K_UP:
                    if active is 0: active  = len(selectable)-1
                    else:           active -= 1
                # move down in menu options
                elif event.key == pygame.K_DOWN:
                    if active is len(selectable)-1: active = 0
                    else:                           active += 1
            self.items[selectable[active]].activate()




def launch(screen,items):
    print "RENDER MENU"
    menu = Menu(screen,items)
    return menu.choose()
