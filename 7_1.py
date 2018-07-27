def isArm(x):
    temp=x
    ord=0
    while temp!=0:
        ord+=1
        temp//=10
    sum=0
    while x>0:
        r=x%10
        sum=sum+pow(r,ord)
        x//=10
    return sum


print("The following are Armstrong numbers in the interval 1-100:")
for i in range(1,101):
    if isArm(i)==i:
        print(i,end=', ')