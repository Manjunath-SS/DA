di={'a':50,'e':46,'c':78,'b':65,'d':65}

print("sorted by Name:")
for x in sorted(di):
    print(x,":",di[x])

print("sorted by marks:")
print(sorted( (value,key) for (key,value) in di.items()))