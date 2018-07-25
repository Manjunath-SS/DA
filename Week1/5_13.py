import re

n=input("Enter file name:")
try:
    f=open(n,"r")
    con=f.read()
    print("The following numbers are present in the given file:\n",set(re.findall(r'[0-9]+',con)))
except:
    print("Could not open file:",n)