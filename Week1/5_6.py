n=input("Enter file name:")
try:
    p=open(n,"r")
    con=p.read()
    print("The content of file is as follows:\n",con)
    p.close()
except:
    print("Could not open file:",n)