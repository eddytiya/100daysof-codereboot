#method overriding
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y 


class Circle(shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)
#overriding area function in this
    def area(self):
        return 3.14 *  super().area()
# rec= shape(3,5)
# print(rec.area)    

c = Circle(5)
print(c.area())