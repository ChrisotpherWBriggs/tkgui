from Tkinter import *
import time
import datetime


top = Tk()

h1 = Label(top, text="Product")
h2 = Label(top, text="In Process")
h3 = Label(top, text="Complete")

l1 = Label(top, text="PRO-CIGNA")
l2 = Label(top, text="UR-CIGNA")
l3 = Label(top, text="MC & CR CARE NETWORK")
l4 = Label(top, text="PBM-MAGELLIN RX")
l5 = Label(top, text="LAB CARD")
l6 = Label(top, text="AHDI")
l7 = Label(top, text="BROKER")
l8 = Label(top, text="TELADOC")
l9 = Label(top, text="COBRA")

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()
CheckVar11 = IntVar()
CheckVar12 = IntVar()
CheckVar13 = IntVar()
CheckVar14 = IntVar()
CheckVar15 = IntVar()
CheckVar16 = IntVar()
CheckVar17 = IntVar()
CheckVar18 = IntVar()

C1 = Checkbutton(top, variable = CheckVar1,
                 onvalue = "Yes", offvalue = "No", height=2)
C2 = Checkbutton(top, variable = CheckVar2,
                 onvalue = "Yes", offvalue = "No", height=2)
C3 = Checkbutton(top, variable = CheckVar3,
                 onvalue = "Yes", offvalue = "No", height=2)
C4 = Checkbutton(top, variable = CheckVar4,
                 onvalue = "Yes", offvalue = "No", height=2)
C5 = Checkbutton(top, variable = CheckVar5,
                 onvalue = "YES", offvalue = "No", height=2)
C6 = Checkbutton(top, variable = CheckVar6,
                 onvalue = "Yes", offvalue = "No", height=2)
C7 = Checkbutton(top, variable = CheckVar7,
                 onvalue = "Yes", offvalue = "No", height=2)
C8 = Checkbutton(top, variable = CheckVar8,
                 onvalue = "Yes", offvalue = "No", height=2)
C9 = Checkbutton(top, variable = CheckVar9,
                  onvalue = "Yes", offvalue = "No", height=2)
C10 = Checkbutton(top, variable = CheckVar10,
                 onvalue = "Yes", offvalue = "No", height=2)
C11 = Checkbutton(top, variable = CheckVar11,
                 onvalue = "Yes", offvalue = "No", height=2)
C12 = Checkbutton(top, variable = CheckVar12,
                 onvalue = "Yes", offvalue = "No", height=2)
C13 = Checkbutton(top, variable = CheckVar13,
                 onvalue = "Yes", offvalue = "No", height=2)
C14 = Checkbutton(top, variable = CheckVar14,
                 onvalue = "YES", offvalue = "No", height=2)
C15 = Checkbutton(top, variable = CheckVar15,
                 onvalue = "Yes", offvalue = "No", height=2)
C16 = Checkbutton(top, variable = CheckVar16,
                 onvalue = "Yes", offvalue = "No", height=2)
C17 = Checkbutton(top, variable = CheckVar17,
                 onvalue = "Yes", offvalue = "No", height=2)
C18 = Checkbutton(top, variable = CheckVar18,
                  onvalue = "Yes", offvalue = "No", height=2)

h1.grid(row=0)
h2.grid(row=0, column=1)
h3.grid(row=0, column=3)

l1.grid(row=1, sticky=W, padx=2)
l2.grid(row=2, sticky=W, padx=2)
l3.grid(row=3, sticky=W, padx=2)
l4.grid(row=4, sticky=W, padx=2)
l5.grid(row=5, sticky=W, padx=2)
l6.grid(row=6, sticky=W, padx=2)
l7.grid(row=7, sticky=W, padx=2)
l8.grid(row=8, sticky=W, padx=2)
l9.grid(row=9, sticky=W, padx=2)

C1.grid(row=1, column=1)
C2.grid(row=2, column=1)
C3.grid(row=3, column=1)
C4.grid(row=4, column=1)
C5.grid(row=5, column=1)
C6.grid(row=6, column=1)
C7.grid(row=7, column=1)
C8.grid(row=8, column=1)
C9.grid(row=9, column=1)

C10.grid(row=1, column=3)
C11.grid(row=2, column=3)
C12.grid(row=3, column=3)
C13.grid(row=4, column=3)
C14.grid(row=5, column=3)
C15.grid(row=6, column=3)
C16.grid(row=7, column=3)
C17.grid(row=8, column=3)
C18.grid(row=9, column=3)

top.mainloop()