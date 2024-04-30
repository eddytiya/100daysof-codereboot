#day66(instance variable and class variable)

class employee:
    def __init__(self,name):
        self.name=name
    def showDetails(self):
        print(f"the name os the employee is {self.name}") 

emp1=employee("adotya")

emp1.showDetails()#use this or

employee.showDetails(emp1)           






#instance variables
class employee:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02#this is instance variable
    def showDetails(self):
        print(f"the name os the employee is {self.name} and the raise amount is {self.raise_amount}") 

emp1=employee("adotya")
emp1.showDetails()
emp1.raise_amount=0.3
emp1.showDetails()

emp2=employee("virot")
emp2.showDetails()



#class variable

class employee:
    company_nae="apple"#class variable
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showDetails(self):
        print(f"the name os the employee is {self.name} and the raise amountin {self.company_nae} is {self.raise_amount}") 

emp1=employee("adotya")
emp1.showDetails()
emp1.raise_amount=0.3
emp1.company_nae="apple india"
emp1.showDetails()

emp2=employee("virot")
emp2.showDetails()
