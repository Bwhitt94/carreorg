import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets\Enemy.png")
        self.rect = self.image.get_rect()
        self.reset_position()
    
    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self, speed, score):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > SCREEN_HEIGHT):
            score += 1
            self.rect.top = 0
            self.reset_position()
        return score

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
