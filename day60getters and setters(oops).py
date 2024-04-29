#getters and setters(oops)

class myclass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")    

    @property#do can use getter using this
    def ten_value(self):
        return 10 * self._value  
#setter
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
        return 10 * self._value  

obj=myclass(10)
obj.ten_value=67
print(obj.ten_value)#getter
obj.show()

