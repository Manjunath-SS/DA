x=input("Enter string1:")
y=input("Enter string2:")
inte=set(x).intersection(set(y))
if not inte:
    print("\nThere is no common letter")
else:
    print(inte)