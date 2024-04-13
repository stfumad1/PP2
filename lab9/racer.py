import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_WEIGHTS = [1, 2, 3]
N = 5

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
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
        pass  

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-5, 0)

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice(COIN_WEIGHTS)  
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
 
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


player = Player()
obstacles = pygame.sprite.Group()
coins = pygame.sprite.Group()  

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        player.move_left()
    elif pressed_keys[K_RIGHT]:
        player.move_right()

    DISPLAYSURF.blit(background, (0, 0))

    player.move()  
    DISPLAYSURF.blit(player.image, player.rect)

    if random.randint(0, 2 * FPS) == 0:
        coin = Coin()
        coins.add(coin)

    for coin in coins:
        coin.move()
        DISPLAYSURF.blit(coin.image, coin.rect)

    if SCORE >= N:
        SPEED += 1
        SCORE = 0  

    if random.randint(0, 2 * FPS) == 0:
        obstacle = Obstacle()
        obstacles.add(obstacle)

    for obstacle in obstacles:
        obstacle.move()
        DISPLAYSURF.blit(obstacle.image, obstacle.rect)

    collected_coins = pygame.sprite.spritecollide(player, coins, True)  
    for coin in collected_coins:
        SCORE += coin.weight  

    if pygame.sprite.spritecollideany(player, obstacles):
        pygame.mixer.Sound('crash.wav.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    coin_counter_text = font_small.render("Coins: " + str(SCORE), True, WHITE)
    coin_counter_rect = coin_counter_text.get_rect()
    coin_counter_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coin_counter_text, coin_counter_rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
