#day71
#dir,dict and help methods

#1.dir
x = [1, 2, 3]
print(dir(x))

print(x.__add__)


#2.dict

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1


p=Person("john",30)
print(p.__dict__)

print(help(Person))
