c:
 cd c:\program files (x86)\gnuwin32\bin 
 awk -F"," "{ if ($4 == "487") print $0 }" "C:\Users\CBriggs\Desktop\Python Scripts\claims.csv" > "C:\Users\CBriggs\Desktop\Python Scripts\result.csv"