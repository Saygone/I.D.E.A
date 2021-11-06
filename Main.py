import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

import First
import Second

c = len(Second.Second_w)

if Second.Second_w[c - 1] == 'а' and 'я':
    First.First_w = First.First_w[:-2]
    First.First_w = First.First_w + 'ая'

root = Tk()
root.title("I.D.E.A")
root.geometry("400x500")

canvas = tkinter.Canvas(root, height=500, width=400)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=201, y=250, anchor=CENTER)

root.mainloop()
