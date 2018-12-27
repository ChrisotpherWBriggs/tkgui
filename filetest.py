import os
import csv
import re
os.chdir("C:\Users\CBriggs\Desktop\Python Scripts")

s1= raw_input("Enter Last Name")
s2 = raw_input("Enter First Name")
s3 = raw_input("Enter Group Number")
s4 = raw_input("Search Claims From Date (mm/dd/yyyy")
s5 = raw_input("Search Claims Through Date (mm/dd/yyyy")


pattern = re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")

fDate = s4.split("/")
fDate2 = (fDate[2] + fDate[0] + fDate[1])

tDate = s5.split("/")
tDate2 = (tDate[2] + tDate[0] + tDate[1])

if re.match(pattern, s4):
    print(s4.split("/"))
else:
    print("no")
csvfile = open("claims.csv", "r")
outfile = open("1.txt", "wb")
outfile2 = csv.writer(outfile)
readCSV = csv.reader(csvfile)

for row in readCSV:
    z = row[4].split("/")
    y = (z[2] + z[0] + z[1])
    if y >= fDate2 and y <= tDate2:
        outfile2.writerow(row)




    """
def claimSearch():
    if s1.upper() and s2.upper() and s3.upper():
        for row in readCSV:
            if s1.upper() and s2.upper() and s3.upper() in row:
                outfile2.writerow(row)
    elif s1.upper() and s2.upper() and not s3.upper():
        for row in readCSV:
            if s1.upper() and s2.upper() in row:
                outfile2.writerow(row)
    elif s1.upper() and s3.upper() and not s2.upper():
        for row in readCSV:
            if s1.upper() and s3.upper() in row:
                outfile2.writerow(row)
    elif s2.upper() and s3.upper() and not s1.upper():
        for row in readCSV:
            if s2.upper() and s3.upper() in row:
                outfile2.writerow(row)
    elif s1.upper() and not s2.upper() and not s3.upper():
        for row in readCSV:
            if s1.upper() in row:
                outfile2.writerow(row)
    elif s2.upper() and not s1.upper() and not s3.upper():
        for row in readCSV:
            if s2.upper() in row:
                outfile2.writerow(row)
    elif s3.upper() and not s1.upper() and not s2.upper():
        for row in readCSV:
            if s3.upper() in row:
                outfile2.writerow(row)
    else:
        print("no terms found")

claimSearch()
"""
csvfile.close()
outfile.close()












