# day78:single inheritance

'''
syntax:
class childclass(Parentclass):
#classbody
'''

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(Self):
        print("sound made by the animal")    


class dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species=dog)
        self.breed=breed

    def make_sound(self):
        print("bark")  

class cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="cat")
        self.breed=breed

    def make_sound(Self):
        print("meow")   
                

d=dog("dog","dopperman")
d.make_sound()

a=Animal("dog","puppy")
a.make_sound()

c=cat("cat","catty")
c.make_sound()

b=Animal("cat","catie")
b.make_sound()