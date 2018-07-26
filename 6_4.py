import math 

def isPalin(x):
    x=str(x)
    if x==x[::-1]:
        print("\t\t",x," is PALINDROME")

def isPrime(x):
    if x==1 or x%2==0:
        return
    else:
        for i in range(3,int(math.sqrt(x))+1):
            if x%i==0:
                return
    print(x," is Prime number")
    isPalin(x)

for i in range(900,1001):
    isPrime(i)