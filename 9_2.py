import math

class shape():
    def area(self,r,b=None,c=None):
        if b==None:
            print("Area of circle is:",r*math.pi*r)
        elif c==None:
            print("Area of rectangle is:",r*b)
        else:
            p=(r+b+c)/2
            print("Area of triangle is:",math.sqrt(p*(p-r)*(p-b)*(p-c)))

class animal():
    sound="animal"
    def mysound(self):
        print("Animal sound")

class lion(animal):
    sound="roar"
    def mysound(self):
        super().mysound()
        print("roar")

class bird(animal):
    sound="chirp"
    def mysound(self):
        super().mysound()
        print("chirp")

x=shape()
#circle
x.area(4)
#rectangle
x.area(2,4)   
#triangle
x.area(4,5,6)         

l=lion()
b=bird()
l.mysound()
b.mysound()