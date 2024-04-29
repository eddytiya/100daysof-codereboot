#constructors(oops)


#we created this in the previous day
#consider this just to understand class
#any method u write needs self arguement

class person:
    def __init__(self,n,o):
        #print("hey i am a person")
        self.name=n
        self.work=o

    def info(self):
        print(f"{self.name} is a {self.work}")

'''above u will see 3 args are stated
but only 2 are passed below this is because 
self arg is passed as variable stated (a,b,c)
'''

a=person("aditya","developer")
b=person("Divya","HR")
#c=person()#if left empty will show this error:TypeError: person.__init__() missing 2 required positional arguments: 'n' and 'o'
a.info()
b.info()


