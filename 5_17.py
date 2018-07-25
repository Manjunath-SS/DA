import os
try:
    f=open("small.txt","r")
    con=f.read()
    for i in reversed(con):
        print(i,end='')
    f.close()
    
except:
    print("Could not open file small.txt")