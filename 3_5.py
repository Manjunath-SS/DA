li=[1,5,3,4,5,1,3,5,2,1,4]

mydict={}
myeven=[]
myodd=[]
for i in li:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1
    if i%2==0:
        myeven.append(i)
    else:
        myodd.append(i)

print("Number of occurrences is as following:")
for i in mydict:
    print(i,":",mydict[i])

print("Largest even=",max(myeven))
print("Largest odd=",max(myodd))