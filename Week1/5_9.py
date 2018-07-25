n=input("Enter string to append:")
try:
    p=open("sam.txt","a")
    p.write(n)
    print("Appended Successfully")
    p.close()
except:
    print("Could not open file:",n)