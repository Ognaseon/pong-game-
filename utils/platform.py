import pygame
from utils.constant import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, side):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.Surface((20, 100))
        self.image.fill('White')
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.side = side
        self.speed = 10

    def move(self):
        click = pygame.key.get_pressed()
        if self.side == 'left':
            if click[pygame.K_w]:
                self.rect.centery -= self.speed
            elif click[pygame.K_s]:
                self.rect.centery += self.speed

        if self.side == 'right':
            if click[pygame.K_UP]:
                self.rect.centery -= self.speed
            elif click[pygame.K_DOWN]:
                self.rect.centery += self.speed
       

    def update(self):
        self.move()