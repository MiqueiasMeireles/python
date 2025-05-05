from time import sleep
from emoji import emojize
import pygame

for c in range(10,0,-1):
    print(c)
    sleep(1)
print(emojize(':sparkler:' * 5))
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()