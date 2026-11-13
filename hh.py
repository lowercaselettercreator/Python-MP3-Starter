from PIL import Image
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("adi_goldstein-random-thoughts-20586.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(0.1)



