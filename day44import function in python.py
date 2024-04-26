#import function in python
import math

p=math.floor(4.3222)
print(p)


from math import sqrt,pi

result=sqrt(9)*pi
print(result)


from math import * #import everything from math
result=sqrt(9)*pi
print(result)

from math import sqrt as s ,pi as p

pri=s(8)*p
print(pri)

#DIR FUNCTION
print(dir(math))