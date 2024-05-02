#day72:super keyword
'''
super keyword is useful to refer parent classes
it is specially useful when a class inherits from multiple parent classes
and u want to call a method from one of the parent classes
'''

# #eg1
# class ParentClass:
#     def parent_method(self):
#         print("1.This is the parent method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("adi")
#         super().parent_method()
#     def child_method(self):
#         print("2.This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()


#eg2

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class programmer:
#   def __init__(self,name,id,lang):
#     self.name=name
#     self.id=id
#     self.lang=lang

# rohan=Employee("rohan das","420")
# adi=programmer("aditya","2345","python")

# print(rohan.name)


"""in class programmer insted of repeating the 
self.name and all we can use super keyword to improve"""


class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class programmer(Employee):
  def __init__(self,name,id,lang):
    super().__init__(name,id)
    self.lang=lang

rohan=Employee("rohan das","420")
adi=programmer("aditya","2345","python")

print(adi.name)
print(adi.id)
print(adi.lang)
