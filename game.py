import pygame as pg

class Game:
    def __init__(self, WIDTH, HEIGHT, FPS):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = FPS
        self.running = False

    def run(self):
        self.running = True

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            pg.display.flip()
            self.clock.tick(self.FPS)
            pg.display.set_caption(str(int(self.clock.get_fps())))
        pg.quit()