from Tkinter import *
from tkFileDialog import*
import sqlite3

#---------sql----


#------------Program----------
def fileOpen():
    filename = askopenfilename(initialdir="C:")
def doNothing():
    print("Worked")
root = Tk()
img1 = PhotoImage(file="C:\\Users\\CBriggs\\Desktop\\icons\\folder.gif")

# *** Main Menu ***

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=fileOpen)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# *** Toolbar ***

toolbar = Frame(root)
insert = Button(toolbar, image=img1, text="Insert Image", command=fileOpen)

insert.pack(side=LEFT, padx=2, pady=2)
printx = Button(toolbar, text="Print", command=doNothing)
printx.pack(side=LEFT, padx=2, pady=2)

#*** Status Bar ***

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)


status.pack(side=BOTTOM, fill=X)
toolbar.pack(side=TOP, fill=X)
root.mainloop()