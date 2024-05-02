# #day70:Class Methods as Alternative Constructors

# '''the basic code without class method'''
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary


# e1=employee("aditya",12000)
# print(e1.name)
# print(e1.salary)    

# #kisi ne kaha hum data tumko line 9 k format mein nhi
# #string k format mein denge
# string="virat-18"
# e2=employee(string.split("-")[0],string.split("-")[1])
# print(e2.name)
# print(e2.salary) 

# #lekin aapko ye bhout time aur ugly laegea toh koi aur tarika delhne padega
# '''the code with class method'''
# #eg1
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])    


# e1=employee("aditya",12000)
# print(e1.name)
# print(e1.salary)    

# #kisi ne kaha hum data tumko line 9 k format mein nhi
# #string k format mein denge
# string="virat-18"
# e2=employee.fromstr(string)
# print(e2.name)
# print(e2.salary) 

# string="rohit-45"
# e2=employee.fromstr(string)
# print(e2.name)
# print(e2.salary) 




'''another example'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
person=Person.from_string("adi,21")
print(person.name)
print(person.age)    