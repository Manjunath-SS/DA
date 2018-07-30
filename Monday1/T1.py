# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:05:31 2018

@author: Manjunath
"""

import re
sen=input("Enter the paragraph:")
senCount=len(re.findall(r"[\w\s\d]*[\.,]",sen))

assert senCount>3, "Number of sentences entered is less than 4, hence exiting"
print("Entered paragraph is:",sen)

mySecReg=r"([\w\d\s]*[\.,]) ([\w\s\d]*[\.,])"
myFirst=re.search(mySecReg,sen)

sen=sen.replace(myFirst.group(2), "UST Global specializes in Healthcare, Retail & Consumber Goods, Banking & Financial Services, Media & Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities")
print("\n After updating second sentence:\n",sen)

vowelCount=len(re.findall(r"a|e|i|o|u|A|E|I|O|U",sen))
print("\nNumber of vowels:", vowelCount)

upperCount=len(re.findall(r"[A-Z]",sen))
print("Number of upper characters:",upperCount)

lowerCount=len(re.findall(r"[a-z]",sen))
print("Number of lower characters:",lowerCount)

specialCount=len(re.findall(r"[^\w\d\s]",sen))
print("Number of special characters:",specialCount)

dic={}

'''
ANOMALY
print(sen)

for i in sen.split():
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
'''

words=re.findall(r"[a-zA-Z0-9]+",sen)

for i in words:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1


print("The following are repeating words and their count:(blank line indicates no repeated words)\n")

for i in dic:
    if dic[i]>1:
        print(i,":",dic[i])
 

sen2=re.findall(r"[\w\d\s]*",sen)
noSpe=''

for i in sen2:
    noSpe+=i

print("\n\nAfter removing special characters:\n",noSpe)

senRegex=r"[\w\s\d]*[\.,]"
senwise=re.findall(senRegex,sen)

mid=""
for i in senwise[1:len(senwise)-1]:
    mid+=i

senwise=str(senwise[len(senwise)-1])+mid+str(senwise[0])
print("\nAfter swapping:\n")

for i in senwise:
    print(i, end="")

'''
firstReg=r"^[\w\s\d]*[\.,]"
lastReg=r"[\w\d\s]*[\.,]$"
f=str(re.findall(firstReg,sen))
l=str(re.findall(lastReg,sen))
m=sen.replace(str(f),"las")
print(f)
print(l)
print(m)


ANOMALY

middleReg=r"(^[\w\d\s]*[\.,])([\w\d\s]*[\.,])([\w\d\s]*[\.,]$)"

f=str(re.findall(firstReg,sen))
l=str(re.findall(lastReg,sen))
m=re.search(middleReg,sen)
print(sen)
print("here\n\n",m.group(3))
'''