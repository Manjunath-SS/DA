li=[5,2,3,1,7]
sqli=[]
for i in range(0,len(li)):
    sqli.append(li[i]*li[i])
ans=zip(li,sqli)
print(type(ans))
print(sorted(list(ans)))