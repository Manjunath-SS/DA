x=input("Enter string:")
di={}
for i in x.split():
    if i in di:
        di[i]+=1
    else:
        di[i]=1

print(di)