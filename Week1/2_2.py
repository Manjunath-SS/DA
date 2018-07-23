# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:42:03 2018

@author: user
"""
import sys

def myFact(x):
    if x==0:
        return 1
    else:
        return(myFact(x-1)*x)
        
def myFibo(x):
    if x<=0:
        return x
    else:
        return myFibo(x-1)+myFibo(x-2)
        
n=int(input("Number:"))
if n<0:
    print("Please enter a positive number")
else:
    print("Factorial=",myFact(n))
    print("\n Fibonacci Series: ")
    for i in range(0,n+1):
        print(myFibo(i))
        i+=1