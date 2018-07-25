import math

x=int(input("Enter beginning range:"))
y=int(input("Enter ending range:"))
print("All Numbers in a range which are Perfect Squares and Sum of all Digits in the Number is Less than 10 are:")
for i in range(x,y+1):
    if math.sqrt(i).is_integer():
        num=i
        sum=0
        while i!=0:
            r=i%10
            sum+=r
            i=i//10
        if sum<10:
            print(num)
            