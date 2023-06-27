import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Music Player")
root.geometry('820x390')
root.resizable(False,False)
mixer.init()

image = Image.open("Mp3n.png")
resize_image = image.resize((795,120))
log = ImageTk.PhotoImage(resize_image)
tk.Label(root, image=log).place(x = 10,y = 0)

button_frame = tk.LabelFrame(root, text='Control Buttons', bg='Turquoise', width=390, height=250)
button_frame.place(x=8,y=130)
listbox_frame = tk.LabelFrame(root, text='Playlist', bg='Grey')
listbox_frame.place(x=398, y=130, height=250, width=410)

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(tk.END, song)

def PlayMusic():
    Music_Name = Playlist.get(tk.ACTIVE)
    print("Currently playing: "+Music_Name[0:-4])
    mixer.music.load(Playlist.get(tk.ACTIVE))
    mixer.music.play()

browse = tk.Button(root, text = "Open Folder", bg = 'green', font = ('bold',10), command = AddMusic)
browse.place(x = 305, y = 150, width = 80, height = 40)
Playlist = tk.Listbox(root, font=("Times new roman", 14), bg="black", fg="white", selectbackground="violet")
Playlist.place(x = 407, y = 160, width = 392, height = 195)

des = tk.Label(root, text = "pause", bg = 'orange').place(x = 105, y = 165)
image = Image.open("pause.png")
resize_image = image.resize((60,60))
img1 = ImageTk.PhotoImage(resize_image)
tk.Button(root, image=img1, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=90, y=190)

des = tk.Label(root, text = "play", bg = 'orange').place(x = 174, y = 165)
image = Image.open("play.png")
resize_image = image.resize((60,60))
img2 = ImageTk.PhotoImage(resize_image)
tk.Button(root, image=img2, bg="#0f1a2b", bd=0, command = PlayMusic).place(x=160, y=190)

des = tk.Label(root, text = "resume", bg = 'orange').place(x = 100, y = 325)
image = Image.open("resume.png")
resize_image = image.resize((60,60))
img3 = ImageTk.PhotoImage(resize_image)
tk.Button(root, image=img3, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=90, y=260)

des = tk.Label(root, text = "stop", bg = 'orange').place(x = 174, y = 325)
image = Image.open("stop.jpg")
resize_image = image.resize((60,60))
img4 = ImageTk.PhotoImage(resize_image)
tk.Button(root, image=img4, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=160, y=260)

root.mainloop()