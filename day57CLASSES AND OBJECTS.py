#CLASSES AND OBJECTS

class person:
    name="aditya"
    occupation="persuaing goodness"
    networth=100000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
print(a.name,':',a.occupation)  

#but suppose u didint like the name or change the name 

a.name="virat"
a.occupation="cricketer"
print(a.name,':',a.occupation)

a.info()

b.name="nitika"
b.occupation="HR"
b.info()