#day65 static methods in python

class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num+=n 

    @staticmethod#ye use karne pe self daalne ki zarurat nahi
    def add(a,b):
        return a + b 
    
#result = math.add(1,2)
#print(result)

a=math(5)
print(a.num)   

a.addtonum(6)
print(a.num) 

print(a.add(7,2))

#suppose u want to add a utility method
#we can create static method

'''
interview
kya class mein self dalna imp hai
ANS:yes it is sometomes important but we can also use @staticmethod for the same


'''

