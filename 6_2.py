import re

inSt="#Python is an interpreted high level programming language for general-purpose programming*."
con=re.findall(r'[\s\d\w]*',inSt)
s1=''
for i in con:
    s1+=i
print(s1)

print("\nPalindrome in string is:")
for i in inSt.split():
    if i == i[::-1]:
        print(i)
        
print("\nRepeating words and occurrences are as follows:\n")
di={}
for i in s1.split():
    if i in di:
        di[i]+=1
    else:
        di[i]=1
        
for i in di:
    if di[i]>1:
        print(i,di[i])