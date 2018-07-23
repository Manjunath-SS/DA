import re

x=input("Enter string:")
print("Index of each characters is as follows:")
for i in x:
    print(i,":",x.index(i))

print("Number of vowels=",len(re.findall(r'a|e|i|o|u|A|E|I|O|U',x)))