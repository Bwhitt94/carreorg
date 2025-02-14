import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_r, K_SPACE
import time
from config import SCREEN_HEIGHT, SCREEN_WIDTH, INITIAL_SPEED, FPS, FONT_SMALL, BLACK
from sprites import Enemy, Player
from game_states import StartMenu, GameOver

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        
        # Load background
        self.background = pygame.image.load("assets\AnimatedStreet.png")
        
        # Game state
        self.reset_game()
        
        # Initialize states
        self.start_menu = StartMenu()
        self.game_over = GameOver()
        
        # Set up speed increase event
        self.INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(self.INC_SPEED, 1000)

    def reset_game(self):
        self.game_state = "start_menu"
        self.score = 0
        self.speed = INITIAL_SPEED
        
        # Initialize sprites
        self.player = Player()
        self.enemy = Enemy()
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.enemy)
        self.all_sprites.add(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == self.INC_SPEED:
                self.speed += 2
            if event.type == QUIT:
                return False
            if event.type == KEYDOWN and event.key == K_r and self.game_state == "game_over":
                self.reset_game()
        return True

    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.game_state == "start_menu" and keys[K_SPACE]:
            self.game_state = "game"
            
        if self.game_state == "game":
            self.score = self.enemy.move(self.speed, self.score)
            self.player.move()
            
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                try:
                    pygame.mixer.Sound('assets\crash.wav').play()
                except pygame.error:
                    print("Warning: crash.wav not found")
                    
                time.sleep(0.5)
                self.game_state = "game_over"
                self.game_over.draw(self.screen)
                pygame.display.update()
                time.sleep(2)
        return True

    def draw(self):
        if self.game_state == "start_menu":
            self.start_menu.draw(self.screen)
        elif self.game_state == "game":
            self.screen.blit(self.background, (0, 0))
            scores = FONT_SMALL.render(str(self.score), True, BLACK)
            self.screen.blit(scores, (10, 10))
            
            for entity in self.all_sprites:
                self.screen.blit(entity.image, entity.rect)
        elif self.game_state == "game_over":
            self.game_over.draw(self.screen)
        
        pygame.display.update()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if not running:
                break
                
            running = self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
