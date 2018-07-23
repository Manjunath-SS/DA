x=input("Enter string:")
y=''
for i in range(2,len(x),2):
    y+=x[i]
print("String after removing odd index values:",y)

myDict=dict()
for x in x.split():
    if x in myDict:
        myDict[x]+=1
    else:
        myDict[x]=1

print("word wise occurance:")
for key in myDict:
    print(key,":",myDict[key])