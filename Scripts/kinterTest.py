from Tkinter import *

root = Tk()
root.geometry("1024x768")
def change_case(event=None):
    new_text = str.swapcase(lab["text"])
    lab.config(text=new_text)

def red_text(event=None):
    lab.config(fg="red")

def black_text(event=None):
    lab.config(fg="black")

w = Label(root, text="Hello World")
lab = Label(root,text="this is a test")

lab.bind("<Button-1>",change_case)
lab.bind("<Enter>",red_text)
lab.bind("<Leave>",black_text)


w.grid()
lab.grid()
root.mainloop()