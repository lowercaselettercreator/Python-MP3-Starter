from PIL import Image
import time
import pygame
pygame.mixer.init()
musicplaylist = ["Air raid siren", "adi_goldstein-random-thoughts-20586", "Let It Grow The Lorax Family Flicks", "Squishmallows Song - Lyric Video"]

def printer():
    for i in musicplaylist:
        print(i)

printer()
songinput = input("AHHHHHHHHH ")
pygame.mixer.music.load(f"music\{songinput}.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy:
    time.sleep(0.1)
