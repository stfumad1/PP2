import pygame
import os
FPS=60

pygame.init()
i = 0
songs = ["C:\\Users\\user\\Downloads\\song1.mp3",
        "C:\\Users\\user\\Downloads\\song2.mp3",
          "C:\\Users\\user\\Downloads\\song3.mp3"]
pygame.mixer.music.load(songs[i])
image_path = "C:\\Users\\user\\Downloads\\musicpic.jpg"
image = pygame.image.load(image_path)
pygame.mixer.music.play(0)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
running = True
while running:
    screen.fill((255, 255, 255))
   
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # pause on space
                pygame.mixer.music.pause()
            if event.key == pygame.K_u:  # unpause
                pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:  # next
                if i < len(songs)-1:
                    i += 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_LEFT:  # prev
                if i > 0:
                    i -= 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
clock.tick(FPS)
screen.blit(image , (0,0))
pygame.quit()