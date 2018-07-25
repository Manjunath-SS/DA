mydict={'5':'five','1':'one'}
x=input("Enter the key:")
if x in mydict:
    print("The value of given key is:",mydict[x])
else:
    print("Key does not exist")