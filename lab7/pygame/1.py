import pygame

pygame.init()
screen = pygame.display.set_mode((500 , 500))

WHITE = (255 , 255 , 255)
BLUE = (0 ,10 ,255)
BLACK = (0 , 0 ,0)
FPS = 60
running = True
clock = pygame.time.Clock()
while running :
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen , BLUE , (100, 100),25 )
    pygame.display.flip()
    clock.tick(FPS)