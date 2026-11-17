from PIL import Image
import time
import pygame
pygame.mixer.init()
musicplaylist = ["Air raid siren.mp3", "adi_goldstein-random-thoughts-20586.mp3", "Let It Grow The Lorax Family Flicks.mp3", "Squishmallows Song - Lyric Video.mp3"]

def printer():
    for i in musicplaylist:
        print(i)

printer()
songinput = input("AHHHHHHHHH")
pygame.mixer.music.load(songinput)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy:
    time.sleep(0.1)


