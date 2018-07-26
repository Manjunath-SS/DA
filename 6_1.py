a = ([['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95]])

mod=[]
for i in a:
    mod.append(i[0:2])
print("The required format is:\n",mod)

a[2]=['Sam',82,79,88,97,99]
print("After update:\n",a[2])

a[0][3]=95

con=[73,80,85]
for i,j in zip(a,con):
   i.append(j)

print("Final:\n",a)