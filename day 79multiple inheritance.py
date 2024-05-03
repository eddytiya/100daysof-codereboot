#multiple inheritance

'''
syntax

class childclass(parentclass1,parentclass2,parentclass3):
#class body
'''

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"the dance is {self.dance}")


class Dancer:
  def __init__(self, dance):
    self.dance = dance   


class DancerEmployee(Employee,Dancer):
  def __init__(self, dance,name):
    self.dance=dance
    self.name=name


o=DancerEmployee("kathak","shivani")
print(o.name)    
print(o.dance)
o.show()


#special mro method

print(DancerEmployee.mro())