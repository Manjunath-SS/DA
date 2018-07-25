x=input("Enter string1:")
y=input("Enter string2:")
xMy=set(x)-set(y)
if not xMy:
    print("\nThere is no letter in the first string that is not in the second string")
else:
    print(xMy)