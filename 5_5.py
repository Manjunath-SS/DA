x=input("Enter string1:")
y=input("Enter string2:")
uniq=set(x).union(set(y))-set(x).intersection(set(y))
if not uniq:
    print("\nThere are no unique letters")
else:
    print(uniq)