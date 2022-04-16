import os
from pygame import mixer
from tkinter import *

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()


def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()


def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()


def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()


root = Tk()
root.title('Music player project')

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")

playlist = Listbox(root, selectmode=SINGLE, bg="#000957", fg="WHITE", font=('roboto', 16), width=62, height=20)
playlist.grid(columnspan=9)

os.chdir(r'C:\music')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="play", command=playsong)
playbtn.config(font=('Verdana', 18), bg="#577BC1", fg="WHITE", width=12)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.config(font=('Verdana', 18), bg="#577BC1", fg="WHITE", width=12)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.config(font=('Verdana', 18), bg="#577BC1", fg="WHITE", width=12)
stopbtn.grid(row=1, column=3)

Resumebtn = Button(root, text="Resume", command=resumesong)
Resumebtn.config(font=('Verdana', 18), bg="#577BC1", fg="WHITE", width=12)
Resumebtn.grid(row=1, column=2)

'''
path = 'C:\\music'
files=os.listdir(path)
folder=random.choice(files)
songpath=(r'C:/music{folder}')
songlist=os.listdir(songpath)
song=random.choice(songlist)
chosensong=(r'C:/music/{folder}/{song}')
os.startfile(chosensong)
'''

mainloop()
