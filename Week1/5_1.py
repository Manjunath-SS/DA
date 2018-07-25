import re

s=input("Enter a string:")
myset=set(s.lower())
print(len(re.findall(r"a|e|i|o|u",str(myset))))