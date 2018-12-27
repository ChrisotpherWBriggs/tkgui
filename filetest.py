import os
import csv
os.chdir("C:\Users\CBriggs\Desktop\Python Scripts")

s1= raw_input()
s2 = raw_input()
s3 = raw_input()

csvfile = open("claims.csv", "r")
outfile = open("1.txt", "wb")
outfile2 = csv.writer(outfile)
readCSV = csv.reader(csvfile)

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
csvfile.close()
outfile.close()












