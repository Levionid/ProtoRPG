import pygame as pg
from Button import Button
import time
import math

class Menu:
    def __init__(self, screen: pg.Surface, 
                 settings: dict,
                 playDef, 
                 settingsDef, 
                 quitDef):
        self.playDef = playDef
        self.settingsDef = settingsDef
        self.quitDef = quitDef

        buttons_size = (516/settings["GUI_SIZE"], 116/settings["GUI_SIZE"])

        self.play_button = Button(screen.get_width()/2, screen.get_height()/10*4.5, 
                                  *buttons_size, "assets/play_button.png")
        
        self.settings_button = Button(screen.get_width()/2, screen.get_height()/10*4.5+buttons_size[1], 
                                      *buttons_size, "assets/settings_button.png")
        
        self.quit_button = Button(screen.get_width()/2, screen.get_height()/10*4.5+buttons_size[1]*2, 
                                 *buttons_size, "assets/quit_button.png")
        
        self.title = pg.transform.scale(pg.image.load('assets/title.png'), 
                                        (715/settings["GUI_SIZE"], 118/settings["GUI_SIZE"])).convert_alpha()
        
        self.title_rect = pg.Rect(0, 0, *self.title.get_size())
        self.title_rect.center = screen.get_width()/2, screen.get_height()/10*2

        self.gradient = pg.transform.scale(pg.image.load('assets/gradient.png'), 
                                        (settings["WIDTH"], 394/1080*settings["HEIGHT"])
                                        ).convert_alpha()
        
        self.gradient_rect = pg.Rect(0, settings["HEIGHT"]-self.gradient.get_size()[1], 
                                  *self.gradient.get_size())

    def update(self, screen: pg.Surface):
        feedback = ''

        self.play_button.update(screen)
        self.settings_button.update(screen)
        self.quit_button.update(screen)

        if self.play_button.is_clicked:
            self.playDef()
        if self.settings_button.is_clicked:
            self.settingsDef()
        if self.quit_button.is_clicked:
            self.quitDef()

    def draw(self, screen: pg.Surface):
        screen.fill("#606060")
        screen.blit(self.gradient, self.gradient_rect)

        title_rotated_image = pg.transform.rotate(self.title, math.sin(time.time()%360*2)*5)
        title_rotated_image_rect = pg.Rect(0, 0, *title_rotated_image.get_size())
        title_rotated_image_rect.center = self.title_rect.center
        screen.blit(title_rotated_image, title_rotated_image_rect)

        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)