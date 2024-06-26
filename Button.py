import pygame as pg

class Button:
    def __init__(self, 
                 centerx: float, 
                 centery: float, 
                 width: float, 
                 height: float, 
                 image_path: str):
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = centerx, centery
        
        try:
            self.image = pg.transform.scale(pg.image.load(image_path), (width, height)).convert_alpha()
        except:
            self.image = pg.transform.scale(pg.image.load('assets/error.png'), (width, height)).convert_alpha()

        try:
            self.active_image = pg.transform.scale(pg.image.load(image_path.replace('.png', '_active.png')), (width, height)).convert_alpha()
        except:
            self.active_image = pg.transform.scale(pg.image.load('assets/error.png'), (width, height)).convert_alpha()
        
        self.is_clicked = False
        self.is_collide = False

    def update(self, screen: pg.Surface):
        mouse_position = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()
        if self.rect.collidepoint(mouse_position):
            self.is_collide = True
            if mouse_pressed[0] and not self.is_clicked:
                self.is_clicked = True
        else:
            self.is_collide = False
            
        if not mouse_pressed[0] and self.is_clicked:
            self.is_clicked = False

    def draw(self, screen: pg.Surface):
        if self.is_collide:
            screen.blit(self.active_image, self.rect)
        else:
            screen.blit(self.image, self.rect)