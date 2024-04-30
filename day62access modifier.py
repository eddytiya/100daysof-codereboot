#access modifier

'''
Access Specifiers/Modifiers
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Let us see the each one of access specifiers in detail:

Types of access specifiers
Public access modifier
Private access modifier
Protected access modifier

note:there is no public,private,protected in python'''

#1.1public example1
class employee:
    def __init__(self):
        self.name="adi"

a=employee()
print(a.name)

#1.2.public example2
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"adis")
print(obj.age)
print(obj.name)


#2.1public example1(we cannot access it as we could do in public)
class employee:
    def __init__(self):
        self.__name="aditiya"

a=employee()
#print(a.__name):cannot be acessed directly

print(a._employee__name)#can be accessed indirectly

#3protected

class Student:
    def __init__(self):
        self._name = "rohit"

    def _funName(self):      # protected method
        return "264sharma"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())