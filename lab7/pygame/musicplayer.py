import pygame
import os

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = (255, 0, 0)
GREEN = (10, 255, 30)
BLUE = (10, 10, 255)


image_path = "C:\\Users\\user\\Downloads\\musicpic.jpg"
next_button_path = "C:\\Users\\user\\Downloads\\next.jpg"
previous_button_path = "C:\\Users\\user\\Downloads\\previous.jpg"
stop_button_path = "C:\\Users\\user\\Downloads\\stop.png"

FPS = 60
clock = pygame.time.Clock()

image = pygame.image.load(image_path)
next_button = pygame.image.load(next_button_path)
previous_button = pygame.image.load(previous_button_path)
stop_button = pygame.image.load(stop_button_path)

songs = [
    "C:\\Users\\user\\Downloads\\song1.mp3",
    "C:\\Users\\user\\Downloads\\song2.mp3",
    "C:\\Users\\user\\Downloads\\song3.mp3"
]
current_song_index = 0
paused = False
stopped = True

def play_song():
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

def toggle_pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def stop_song():
    pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pygame.mixer.music.load(songs[current_song_index-1])
            pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if stopped:
                    play_song()
                    stopped = False
                else:
                    toggle_pause()
            elif event.key == pygame.KEYUP:
                pygame.mixer.music.load(songs[current_song_index+1])
            pygame.mixer.music.play()

    screen.blit(image, (0, 0))
    screen.blit(previous_button, (20, 500 ))  # Позиция кнопки предыдущей песни
    screen.blit(next_button, (40 , 500))      # Позиция кнопки следующей песни
    screen.blit(stop_button, (35 , 500))      # Позиция кнопки стоп

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
