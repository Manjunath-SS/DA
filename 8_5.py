x=input("Enter string:")
li=[]
for i in x.split(','):
    li.append(i)
print(sorted(li))