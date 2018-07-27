import re

s=input("Enter a sentence:")
print("Number of letters is:",len(re.findall(r'[a-zA-Z]',s)))
print("Number of digits is:",len(re.findall(r'\d',s)))
