try:
    p=open("sam.txt","r")
    q=open("f2.txt","a+")
    q.write(p.read())
    print("File sam.txt appended into f2.txt")
    p.close()
    q.close()
except:
    print("Could not open file")