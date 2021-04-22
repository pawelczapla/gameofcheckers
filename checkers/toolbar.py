from PIL import ImageTk
import PIL.Image
import os
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("+300+110")
embed = tk.Frame(root, width=200, height=800)
embed.pack(side=LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
newgame = ImageTk.PhotoImage(PIL.Image.open('assets/newgame1.jpg'))
single = ImageTk.PhotoImage(PIL.Image.open('assets/singleplayer1.png'))
multi = ImageTk.PhotoImage(PIL.Image.open('assets/multiplayer1.jpg'))
