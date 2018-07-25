myList=[6,5,4,8,5,3,4,5]
print("The list is:",myList)
print("Largest number in the list is:",max(myList))
print("Second largest number in the list is:",max(sorted(myList)[:len(myList)-1]))
temp1=myList[0]
temp2=myList[len(myList)-1]
myList[len(myList)-1]=temp1
myList[0]=temp2
print("List after swapping is:",myList)