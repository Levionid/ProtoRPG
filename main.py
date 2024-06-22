import pygame as pg
import json
from Menu import Menu
from Game import Game

def main(settings):
    pg.init()

    screen = pg.display.set_mode(size=(settings['WIDTH'], settings['HEIGHT']),
                             flags=pg.FULLSCREEN if settings['FULLSCREEN'] else 0)
    clock = pg.time.Clock()

    application = Menu(screen, settings)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        application_feedback = application.update(screen)
        if application_feedback == 'play':
            application = Game()
        elif application_feedback == 'menu':
            application = Menu(screen, settings)
        elif application_feedback == 'settings':
            pass
        elif application_feedback == 'quit':
            running = False

        application.draw(screen)

        pg.display.flip()
        clock.tick(settings['FPS'])
        pg.display.set_caption(str(int(clock.get_fps())))
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
    
    main(settings)