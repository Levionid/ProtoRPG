import pygame as pg
from Button import Button

class Menu:
    def __init__(self, screen: pg.Surface, settings: dict):
        self.play_button = Button(screen.get_width()/2, screen.get_height()/10*4, 480/settings["GUI_SIZE"], 60/settings["GUI_SIZE"], "assets/play_button.png")
        self.settings_button = Button(screen.get_width()/2, screen.get_height()/10*6, 480/settings["GUI_SIZE"], 60/settings["GUI_SIZE"], "assets/settings_button.png")
        self.quit_button = Button(screen.get_width()/2, screen.get_height()/10*8, 480/settings["GUI_SIZE"], 60/settings["GUI_SIZE"], "assets/quit_button.png")

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
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)