print("Enter multiple lines:")
x=''
while True:
    try:
        line = input()
        x+='MyPrefix_'+line+'\n'
    except EOFError:
        break
print(x)