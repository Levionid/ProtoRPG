from MainMenu import MainMenu
from Game import Game

class Menu:
    def __init__(self):
        self.menu = None
        self.running = False

    def menuDef(self, screen, settings):
        self.menu = MainMenu(screen, settings, self.playDef, self.settingsDef, self.quitDef)

    def playDef(self):
        self.menu = Game()

    def settingsDef(self):
        pass

    def quitDef(self):
        self.running = False