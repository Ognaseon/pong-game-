
import pygame
from .constant import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, collidator, speed):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill('White')
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.bounce = [False, True]
        self.collidator = collidator
        self.speed = speed
    
    def move_y(self):
        if self.rect.bottom >= HEIGHT:
            self.bounce[0] = True
        elif self.rect.top <= 0:
            self.bounce[0] = False
        
        if self.bounce[0] == True:
            self.rect.centery -= self.speed
        else:
            self.rect.centery += self.speed

    def move_x(self):
        if pygame.sprite.spritecollide(self, self.collidator, False):
            self.bounce[1] = not self.bounce[1]

        if self.bounce[1] == False:
            self.rect.centerx -= self.speed
        else:
            self.rect.centerx += self.speed
        



    def update(self):
        self.move_y()
        self.move_x()
