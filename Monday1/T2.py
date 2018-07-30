# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:16:51 2018

@author: Manjunath
"""
import statistics

print("Enter student name followed by 3 marks:")

m=[]
dic={}

for i in range(10):
    n=input("Enter name:")
    m=input("Enter marks:").split()
    dic[n]=m

for i in dic:
    print(i,":\t",dic[i][0],":\t",dic[i][1],":\t",dic[i][2])

s1=[]
s2=[]
s3=[]

for i in dic:
    s1.append(int(dic[i][0]))
    s2.append(int(dic[i][1]))
    s3.append(int(dic[i][2]))

print("Mean of s1:",statistics.mean(s1))
print("Median of s1:",statistics.median(s1))
print("Mean of s2:",statistics.mean(s2))
print("Median of s2:",statistics.median(s2))
print("Mean of s3:",statistics.mean(s3))
print("Median of s3:",statistics.median(s3))

tot=[]
for i in dic:
    tot.append(i)
    tot.append(sum(int(i) for i in dic[i]))

print("Top 3 students are:")

for i in range(0,6,2):
    print(tot[i])

    
for i in dic:
    avg=(sum(int(i) for i in dic[i]))/3
    print(i,end=" secured:")
    if avg>90:
        print("A+")
    elif avg>80:
        print("A")
    elif avg>70:
        print("B+")
    elif avg>60:
        print("B")
    elif avg>50:
        print("C")
    else:
        print("D")