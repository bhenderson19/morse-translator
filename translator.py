from playsound import *
from tkinter import *
import time
import sys
import os

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
morse_long = os.path.join(bundle_dir, 'morse_long.wav')
morse_short = os.path.join(bundle_dir, 'morse_short.wav')

chars = [" ","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
morse = [" ","·----","··---","···--","····-","·····","-····","--···","---··","----·","-----","·-","-···","-·-·","-··","·","··-·","--·","····","··","·---","-·-","·-··","--","-·","---","·--·","--·-","·-·","···","-","··-","···-","·--","-··-","-·--","--··"]

def english2morse(master,e):
    text = e.get().lower()
    morse_string = ""
    for char in text:
        index = chars.index(char)
        morse_char = morse[index]

        time.sleep(0.715)
        for signal in list(morse_char):
            if signal == "-":
                playsound(morse_long) #0.715 secs long (3 time units)
                time.sleep(0.248)
            elif signal == "·":
                playsound(morse_short) #0.248 secs long (1 time unit)
                time.sleep(0.248)
            else:
                time.sleep(1.668)

        morse_string += morse_char+" "

    Label(master,text=morse_string).pack()