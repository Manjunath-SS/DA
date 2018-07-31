n=int(input("Enter number of students:"))
h=[]
w=[]
b=[]
for i in range(n):
    x=int(input("Enter height in m:"))
    y=int(input("Enter weight in kg:"))
    h.append(x)
    w.append(y)
    b.append(y/x*x)
print("The BMI of corresponding weight and heights are as follows:\n",tuple(zip(h,w,b)))