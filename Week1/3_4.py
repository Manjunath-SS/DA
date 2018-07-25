li=[1,2,3,4,5,6,7,8,9,10]
print("List is:",li)
print("Third element=",li[2])
print("Sixth element=",li[5])
print("First 5 elements are",li[:5])
print("Seventh to end",li[7:])
li[1]='x'
li[4]='y'
print("Modified list is:",li)
li.pop(4)
print("After deleting 5th element:",li)
print("Number of elements in list=",len(li))