import re

x=input("Enter words separated by comma:")
x=re.findall(r',?([a-z]*)',x)

y=[]
for i in x:
    if i in y:
        pass
    else:
        y.append(i)
print("Sorted words are=",end='')
for i in sorted(y):
    print(i,end='  ')