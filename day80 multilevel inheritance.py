#multilevel inheritance

'''
class BaseClass:
    # Base class code
    
class DerivedClass1(BaseClass):
    # Derived class 1 code
    
class DerivedClass2(DerivedClass1):
    # Derived class 2 code


like family tree

grandfather is related to father
father is releted to u
therefore u r indeirctly related too your grand father

is A=B & B=C
so A=C

one class is related to another creating multiple class
'''

#https://javatutoring.com/multilevel-inheritance-in-java/
#consider the above link for the image

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o=GoldenRetriever("tommy","black")
o.show_details()

print(GoldenRetriever.mro())

