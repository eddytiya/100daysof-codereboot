#day 69 :class methods

class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and the company name is {self.company}")
    
    @classmethod
    def changeCompany(cls,newCompany):#cls is like self we can write anything on place of self
        cls.company=newCompany

e1=employee()
e1.name="adie"
e1.show()     
e1.changeCompany("tesla")
e1.show()        
print(employee.company)


