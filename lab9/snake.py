import pygame
from random import randrange
RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5
pygame.init()
font = pygame.font.Font(None, 36)
score = 0

# Timer for disappearing food
food_timer = 3000  # Food disappears after 3 seconds
current_time = pygame.time.get_ticks()

sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

running = True

while running:
    sc.fill(pygame.Color('black'))
    # Drawing snake
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]

    # Check if it's time to spawn new food
    if pygame.time.get_ticks() - current_time > food_timer:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        current_time = pygame.time.get_ticks()  # Reset the timer

    # Draw food
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    # Snake move
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
        score += 1

    # Score
    score_text = font.render(f'Score: {score}', True, pygame.Color('white'))
    sc.blit(score_text, (RES - 150, 10))

    # Game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Control
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0

pygame.quit()
