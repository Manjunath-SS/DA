x=input("Enter string1:")
y=input("Enter string2:")
comm=set(x).intersection(set(y))
if not comm:
    print('The given strings have no letters in common')
else:
    print("The following are the common letters:\n",comm)