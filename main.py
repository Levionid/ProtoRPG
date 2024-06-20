import pygame as pg
import json
from game import Game

def main(settings):
    application = Game()

    screen = pg.display.set_mode(size=(settings['WIDTH'], settings['HEIGHT']),
                             flags=pg.FULLSCREEN if settings['FULLSCREEN'] else 0)
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        application.update()

        screen.fill((0, 0, 0))

        application.draw()

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
            "FULLSCREEN": False
            }
        with open('settings.json', 'w') as file:
            json.dump(settings, file)
    
    main(settings)