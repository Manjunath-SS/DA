import math

print("\n1)Factorial\n2)LCM\n3)HCF\n4)Factor\nEnter option:")
n=int(input())
if n==1:
    x=int(input("Enter a number:"))
    print("The factorial of the entered number is:",math.factorial(5))
elif n==2:
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    print("LCM is:",x*y/math.gcd(x,y))
elif n==3:
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    print("HCF is:",math.gcd(x,y))
elif n==4:
    x=int(input("Enter a number:"))
    print("The following are the factors:")
    for i in range(1,x):
        if x%i==0:
            print(i,end=", ")
else:
    print("Invalid option entered")
#print(math.gcd(5,10))