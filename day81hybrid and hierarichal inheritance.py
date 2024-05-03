#hybrid and hierarichal inheritance
#suppose

#hybrid:Hybrid inheritance is a combination 
#of multiple inheritance and single inheritance
class BaseClass:
    pass

class derived1(BaseClass):
    pass

class derived2(BaseClass):
    pass


class derived3(derived1,derived2):
    pass

'''
    CEO
      |
      |
----------------
|     |        |
m1    m2      m3


'''
#hierarichal inheritance

