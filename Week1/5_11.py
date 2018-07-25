try:
    p=open("sam.txt","r")
    q=open("f1.txt","w+")
    q.write(p.read())
    print("File sam.txt copied into f1.txt")
    p.close()
    q.close()
except:
    print("Could not open file")