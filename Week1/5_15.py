try:
    f=open("small.txt","r")
    con=f.read()
    f.close()
    f=open("small.txt","w")      
    f.write(con.title())
    f.close()
    
except:
    print("Could not open file small.txt")