import pygame
from random import randrange
RES = 800
SIZE = 50

x , y = randrange(0, RES , SIZE) , randrange(0 , RES , SIZE)
apple = randrange(0 ,RES , SIZE) , randrange(0, RES,SIZE)
length = 1
snake = [(x ,y)]
dx , dy = 0, 0
fps =5
pygame.init()
font = pygame.font.Font(None ,36)
score = 0

sc = pygame.display.set_mode([RES ,RES])
clock = pygame.time.Clock()

running = True

while running:
    sc.fill(pygame.Color('black'))
        #drawing snake
    [(pygame.draw.rect(sc , pygame.Color('green') , (i , j ,SIZE , SIZE))) for i,j in snake]
    pygame.draw.rect(sc, pygame.Color('red') , (*apple,SIZE,SIZE))
    #snake move
    x +=dx * SIZE
    y +=dy * SIZE
    snake.append((x,y))
    snake = snake[-length:]
     #eating apple
    if snake[-1] == apple:
        apple = randrange(0 ,RES , SIZE) , randrange(0, RES,SIZE)
        length +=1
        fps +=1
        score += 1
    
    #score
    score_text = font.render(f'Score: {score}', True, pygame.Color('white'))
    sc.blit(score_text, (RES - 150, 10))
    #game over
    if x < 0 or x > RES - SIZE or y < 0 or y >RES -SIZE:
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx,dy = 0,-1
    if key[pygame.K_s]:
        dx,dy = 0,1
    if key[pygame.K_a]:
        dx,dy = -1,0
    if key[pygame.K_d]:
        dx,dy = 1,0
            
pygame.quit()

