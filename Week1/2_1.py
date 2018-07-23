# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:33:53 2018

@author: Manjunath
"""
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

n=int(input("Enter a number:"))
sum=isArm(n)
if sum==n:
    print("Entered number is Armstrong number")
else:
    print("Entered number is armstrong number")

print("The following are Armstrong numbers in the interval 1-500:")
for i in range(1,501):
    if isArm(i)==i:
        print(i,end=', ')