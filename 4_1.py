mydict={}
print("Enter Roll no followed by Name of 10 students:")
for i in range(0,10):
    x=input("RollNo:")
    y=input("Name:")
    if x not in mydict:
        mydict[x]=y
    else:
        print("RollNo already exists")