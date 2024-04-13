# Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load images
background = pygame.image.load("AnimatedStreet.png")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.original_image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pass  # Метод будет использоваться для автоматического перемещения в зависимости от нажатых клавиш

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-5, 0)

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

# Setting up Sprites
player = Player()
obstacles = pygame.sprite.Group()

# Create a window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race")

# Game Loop
while True:
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        player.move_left()
    elif pressed_keys[K_RIGHT]:
        player.move_right()

    # Moves background
    DISPLAYSURF.blit(background, (0, 0))

    # Moves and Re-draws all Sprites
    player.move()
    DISPLAYSURF.blit(player.image, player.rect)

    # Добавляем препятствие с частотой 1 раз в секунду
    if random.randint(0, 2 * FPS) == 0:
        obstacle = Obstacle()
        obstacles.add(obstacle)

    for obstacle in obstacles:
        obstacle.move()
        DISPLAYSURF.blit(obstacle.image, obstacle.rect)

    # Check collision
    if pygame.sprite.spritecollideany(player, obstacles):
        pygame.mixer.Sound('crash.wav.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Updates display and sets FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
