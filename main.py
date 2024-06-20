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
        if application_feedback == 'game':
            application = Game()
        elif application_feedback == 'menu':
            application = Menu(screen, settings)

        screen.fill((0, 0, 0))

        application.draw(screen)

        pg.display.flip()
        clock.tick(settings['FPS'])
        pg.display.set_caption(str(int(clock.get_fps())))
    pg.quit()

if __name__ == '__main__':
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
    
    main(settings)