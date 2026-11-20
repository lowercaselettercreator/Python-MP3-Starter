import tkinter as tk
import pygame
pygame.mixer.init()
import time

def playmusic():
    pygame.mixer.music.load(r"music\Air raid siren.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy:
        time.sleep(0.1)

window = tk.Tk()
window.geometry("300x200")

button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="FIRE THE AIR RAID SIREN", command=playmusic).pack(side="left", ipadx=50, ipady=50)
window.mainloop()