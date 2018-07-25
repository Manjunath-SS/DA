n=input("Enter file name:")
try:
    p=open(n,"r")
    con=p.read()
    print(con.count('\n')+1)
    p.close()
except:
    print("Could not open file:",n)