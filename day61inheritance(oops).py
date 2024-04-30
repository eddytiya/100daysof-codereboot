#inheritance(oops)

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"the name of the employee:{self.id} is {self.name}") 
        
#suppose someone ask to change the class from employee to programmer or cricketer
#woh karne pe sab jagah error aa jayegne agar class ko rename kia toh
#we can us einheritance to do the same

#using inheritance to change class employee to programmer

class Programmer(employee):
    def showlanguage(self):
        print("the def lang is python")

e1=employee("rohit sharma","264")
e1.showDetails() 

e2=Programmer("virat kohli","183")
e2.showDetails()   
e2.showlanguage()     