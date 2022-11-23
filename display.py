from tkinter import *
from translator import *

master = Tk()
master.title("Morse Code Translator")
master.geometry("400x100")

Label(master,text="Enter Text").pack()
e = Entry(master)
e.pack()
Button(master,text="Enter",command=lambda: english2morse(master,e)).pack()

mainloop()