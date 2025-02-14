import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, BLACK

class StartMenu:
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 40)
        
    def draw(self, surface):
        surface.fill((0, 0, 0))
        title = self.font.render('My Game', True, WHITE)
        start_button = self.font.render('Press SPACE to Start', True, WHITE)
        
        surface.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, 
                            SCREEN_HEIGHT/2 - title.get_height()/2))
        surface.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2,
                                  SCREEN_HEIGHT/2 + start_button.get_height()/2))

class GameOver:
    def __init__(self):
        self.font = pygame.font.SysFont("Verdana", 60)
        self.text = self.font.render("Game Over", True, BLACK)
        
    def draw(self, surface):
        surface.fill(RED)
        surface.blit(self.text, (30, 250))
