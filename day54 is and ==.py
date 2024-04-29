#'is'VS '==':

'''
is:compares exact location of the object in memory
==:compares values
both are comparative operators
'''


a=4
b="4"
print (a is b)#exact loacation of object in memory
print(a == b )

a=[1,2,43]
b=[1,2,43]
print (a is b)#exact loacation of object in memory
print(a == b)

a=3
b=3
print (a is b)#exact loacation of object in memory
print(a == b)

a="aditya"
b="aditya"
print (a is b)#exact loacation of object in memory
print(a == b)

a=(1,2)
b=(1,2)
print (a is b)#exact loacation of object in memory
print(a == b)

a=None
b=None
print (a is b)#exact loacation of object in memory
print (a is None)
print(a == b)