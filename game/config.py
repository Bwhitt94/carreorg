import pygame

# Game Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
INITIAL_SPEED = 5

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame and fonts
pygame.init()
FONT_LARGE = pygame.font.SysFont("Verdana", 60)
FONT_SMALL = pygame.font.SysFont("Verdana", 20)