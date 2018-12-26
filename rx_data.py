from Tkinter import *
from PIL import ImageTk,Image
import csv
import os




def writebat():
    b2 = search.get()
    os.chdir("C:\Users\CBriggs\Desktop\Python Scripts")
    writing = open("make.bat", "w")
    writing.write("c:\n")
    writing.write(" ")
    writing.write("cd c:\\program files (x86)\\gnuwin32\\bin \n")
    writing.write(" ")
    writing.write("awk -F\",\" \"{ if ($4 == " + "\"" + str(b2) + "\") print $0 }\"" + " \"C:\Users\CBriggs\Desktop\Python Scripts\claims.csv\" > " + "\"C:\Users\CBriggs\Desktop\Python Scripts\\result.csv\"")
    writing.close()
    os.system("make.bat")
    y = []
    infile = open("result.csv", "rb")
    for x in infile:
        y.append(len(x))
    infile.close()
    w = max(y)
    h = len(y)
    new = Toplevel()
    scrollbar = Scrollbar(new)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(new, yscrollcommand=scrollbar.set)
    listbox.config(width=w, height=h)
    infile = open("result.csv", "rb")
    for x in infile:
        listbox.insert(END, str(x))
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=listbox.yview)




root = Tk()
root.title("Rx Tracker")
root.geometry("1024x768")

canvas = Canvas(root,width= 400, height = 125)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(20,20, anchor=NW, image=img)
canvas.config(bg="white")

frame = Frame(root)
frame.pack()

label = Label(frame, text="Enter Group Id: ")
label.pack(side=LEFT)
search = Entry(frame)
search.pack(padx = 10, pady = 5)

b1 = Button(frame, text="Search", command=writebat)

b1.pack()






root.mainloop()




