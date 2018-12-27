from Tkinter import *
from PIL import ImageTk,Image
import csv
import os


#Search function

def claimSearch():
    os.chdir("C:\Users\CBriggs\Desktop\Python Scripts")

    s1= search.get()
    s2 = search1.get()
    s3 = search2.get()

    csvfile = open("claims.csv", "rb")
    outfile = open("result.csv", "wb")
    outfile2 = csv.writer(outfile)
    readCSV = csv.reader(csvfile, delimiter=",")


    if s1 and s2 and s3:
        for row in readCSV:
            if s1.upper() == row[0] and s2.upper() == row[1]  and s3.upper == row[3] :
                outfile2.writerow(row)
    elif s1 and s2 and not s3:
        for row in readCSV:
            if s1.upper() == row[0] and s2.upper() == row[1] in row:
                outfile2.writerow(row)
    elif s1 and s3 and not s2:
        for row in readCSV:
            if s1.upper() == row[0] and s3.upper == row[3] in row:
                outfile2.writerow(row)
    elif s2 and s3 and not s1:
        for row in readCSV:
            if s2.upper() == row[1] and s3.upper == row[3] in row:
                outfile2.writerow(row)
    elif s1 and not s2 and not s3:
        for row in readCSV:
            if s1.upper() == row[0] in row:
                outfile2.writerow(row)
    elif s2 and not s1 and not s3:
        for row in readCSV:
            if s2.upper() == row[1] in row:
                outfile2.writerow(row)
    elif s3 and not s1 and not s2:
        for row in readCSV:
            if s3.upper() == row[3] in row:
                outfile2.writerow(row)
    else:
        print("no terms found")

    csvfile.close()
    outfile.close()

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



#create main window
root = Tk()
root.title("Rx Tracker")
root.geometry("1024x768")

#create canvas
canvas = Canvas(root,width= 400, height = 125)

#image
img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(20,20, anchor=NW, image=img)
canvas.config(bg="white")

#frame
frame = Frame(root)
frame2 = Frame(root)

#labels
label = Label(frame2, text="Enter Last Name:")
label1 = Label(frame2, text="Enter First Name: ")
label2 = Label(frame2, text="Enter Group ID:")
label3 = Label(frame2, text="Enter Beginning Date Range (mm/dd/yyyy)")
label4 = Label(frame2, text="Enter Beginning Date Range (mm/dd/yyyy)")

label.configure()
#entry boxes
search = Entry(frame2)
search1 = Entry(frame2)
search2 = Entry(frame2)
search3 = Entry(frame2)
search4 = Entry(frame2)

#button
b1 = Button(frame2, text="Search", command=claimSearch)

#layout
canvas.grid(row=0, sticky=W)
frame.grid(row=0, pady=25, sticky=W)
frame2.grid(row=1, pady=25, sticky=W)
label.grid(row=1, column=0, padx=20)
search.grid(row=1, column=1, padx=20)
label1.grid(row=2, column=0, padx=20)
search1.grid(row=2, column=1, padx=20)
label2.grid(row=3, column=0, padx=20)
search2.grid(row=3, column=1, padx=20)
label3.grid(row=4, column=0, padx=20)
search3.grid(row=4, column=1, padx=20)
label4.grid(row=5, column=0, padx=20)
search4.grid(row=5, column=1, padx=20)
b1.grid(row=6, columnspan=3, pady=30)







root.mainloop()




