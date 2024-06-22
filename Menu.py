import pygame as pg
from Button import Button

class Menu:
    def __init__(self, screen: pg.Surface, settings: dict):
        self.play_button = Button(screen.get_width()/2, screen.get_height()/10*4.5, 
                                  516/settings["GUI_SIZE"], 116/settings["GUI_SIZE"], 
                                  "assets/play_button.png", "assets/play_button_active.png")
        self.settings_button = Button(screen.get_width()/2, screen.get_height()/10*4.5+116/settings["GUI_SIZE"], 
                                      516/settings["GUI_SIZE"], 116/settings["GUI_SIZE"], 
                                      "assets/settings_button.png", "assets/settings_button_active.png")
        self.quit_button = Button(screen.get_width()/2, screen.get_height()/10*4.5+116/settings["GUI_SIZE"]*2, 
                                  516/settings["GUI_SIZE"], 116/settings["GUI_SIZE"], 
                                  "assets/quit_button.png", "assets/quit_button_active.png")
        self.title = pg.transform.scale(pg.image.load('assets/title.png'), 
                                        (879/settings["GUI_SIZE"], 118/settings["GUI_SIZE"])
                                        ).convert_alpha()
        self.title_rect = pg.Rect(0, 0, 879/settings["GUI_SIZE"], 118/settings["GUI_SIZE"])
        self.title_rect.center = screen.get_width()/2, screen.get_height()/10*2
        self.gradient = pg.transform.scale(pg.image.load('assets/gradient.png'), 
                                        (settings["WIDTH"], 394/1080*settings["HEIGHT"])
                                        ).convert_alpha()
        self.gradient_rect = pg.Rect(0, settings["HEIGHT"]-394/1080*settings["HEIGHT"], 
                                  settings["WIDTH"], 394/1080*settings["HEIGHT"])

    def update(self, screen: pg.Surface) -> str:
        feedback = ''

        self.play_button.update(screen)
        self.settings_button.update(screen)
        self.quit_button.update(screen)

        if self.play_button.is_clicked:
            feedback = 'play'
        if self.settings_button.is_clicked:
            feedback = 'settings'
        if self.quit_button.is_clicked:
            feedback = 'quit'

        return feedback

    def draw(self, screen: pg.Surface):
        screen.fill("#606060")
        screen.blit(self.gradient, self.gradient_rect)
        screen.blit(self.title, self.title_rect)
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)