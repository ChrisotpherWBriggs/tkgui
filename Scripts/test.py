from Tkinter import *
import sqlite3
import tkMessageBox

root = Tk()
x = sqlite3.connect("C:\\Users\\CBriggs\\Documents\\New Database.accdb")

x1 = x.cursor()

search = x1.execute("""SELECT * FROM emp WHERE id=3""")

a = Label(root, text=search)

a.pack()

root.mainloop()
