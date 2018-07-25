try:
    f=open("small.txt","rb+")
    f.seek(0,2)
    l=f.tell()
    st=''
    for i in range(-1,-l-1,-1):
        f.seek(i,2)
        st+=str(f.read(1).decode())
    print(st)
    
   
        
   
    '''f=open("small.txt","r")
    con=f.read()
    for i in reversed(con):
        print(i,end='')'''
    f.close()
    
except:
    print("Could not open file small.txt")