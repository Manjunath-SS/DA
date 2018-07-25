n=input("Enter file name:")
di={}
try:
    p=open(n,"r")
    con=p.read()
    for i in con.split():
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    print("The following are the occurrences:\n")
    for i in di:
        print(i,":",di[i])
    p.close()
except:
    print("Could not open file:",n)