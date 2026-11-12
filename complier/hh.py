from PIL import Image
import pygame
pygame.mixer.init(frequency=16000)

chickenlib = ["adi_goldstein-random-thoughts-20586.mp3", 
              "julytmusic-random-acoustic-electronic-guitar-136427.mp3", 
              "playhousesound-random-drop-play-house-copyright-free-music-206930.mp3"]

pygame.mixer.music.load("C:\Users\aidanz14\Documents\GitHub\Python-MP3-Starter\adi_goldstein-random-thoughts-20586.mp3")
pygame.mixer.music.play()



