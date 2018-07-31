class Animal():
    sound="animal"
    def myprint():
        print(sound)

class Sponge():
    sound="sponge"
    def myprint():
        print(sound)

class Simple(Animal):
    sound="mammal"
    def myprint():
        print(sound)

class MultLevel(Simple):
    sound="Vertebrate"
    def myprint():
        print(sound) 
        
class Mult(Sponge,Animal):
    sound="Multiple"
    def myprint():
        print(sound) 

class Hie(Simple):    
    sound="Hierarchial"
    def myprint():
        print(sound) 
    
ob1=Animal()
print(ob1.myprint)