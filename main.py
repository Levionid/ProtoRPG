import pygame as pg
import json
from Menu import Menu

class Application:
    def __init__(self, settings):
        pg.init()
        self.screen = pg.display.set_mode(size=(settings['WIDTH'], settings['HEIGHT']))
        self.clock = pg.time.Clock()
        self.settings = settings
        self.application = Menu()
        self.application.menuDef(self.screen, self.settings)

    def run(self):
        self.application.running = True

        while self.application.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.application.running = False

            self.application.menu.update(self.screen)
            
            self.application.menu.draw(self.screen)

            pg.display.flip()
            self.clock.tick(settings['FPS'])
            pg.display.set_caption(str(int(self.clock.get_fps())))
        pg.quit()

def get_options() -> dict:
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {
            "WIDTH": 960,
            "HEIGHT": 540,
            "FPS": 60,
            "FULLSCREEN": False,
            "GUI_SIZE": 1
            }
        with open('settings.json', 'w') as file:
            json.dump(settings, file)

    return settings

if __name__ == '__main__':
    settings = get_options()
    
    app = Application(settings)
    app.run()