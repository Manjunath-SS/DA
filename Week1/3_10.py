x=int(input("Enter number of elements to enter:"))
li=[]
for i in range(0,x):
    n=int(input())
    li.append(n)
cs=[]
for i in range(0,x):
    sum=0
    for j in range(0,i+1):
        sum+=li[j]
    cs.append(sum)
    
print("The list is:",li)
print("Required list is:",cs)