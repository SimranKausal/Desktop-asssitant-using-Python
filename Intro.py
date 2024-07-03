import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygame.mixer as mixer
import os

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img_sequence
    img_sequence = Image.open("iron-man-gif-5.gif")
    lbl = tk.Label(root)
    lbl.place(x=0, y=0)
    i=0
    mixer.init()  # Initialize the pygame mixer
    mixer.music.load("rt-4uzaf1ab3ldl7yhof.mp3")
    mixer.music.play()
    frames = [ImageTk.PhotoImage(frame.copy().resize((1000, 500))) for frame in ImageSequence.Iterator(img_sequence)]
    delay = img_sequence.info['duration']
    def update(idx):
        frame = frames[idx]
        lbl.config(image=frame)
        root.after(delay, update, (idx + 1) % len(frames))
    update(0)

root = tk.Tk()
root.geometry("1000x500")

play_gif()
root.mainloop()
