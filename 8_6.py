import re
p=input("Enter the password:")

cap=r'[A-Z]'
spe=r'[^A-Za-z0-9]'
num=r'\d'

capCon=len(re.findall(cap,p))
speCon=len(re.findall(spe,p))
charCon=len(p)
numCon=len(re.findall(num,p))

assert charCon>8, "Minimum of 8 characters is required"
assert capCon>0, "Atleast one capital letter is required"
assert numCon>0, "Atleast one number is required"
assert speCon>0, "Atleast one special character is required"
assert charCon<14, "Maximum of 14 characters is allowed"

print("The entered password is valid")