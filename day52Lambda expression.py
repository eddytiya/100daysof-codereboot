#Lambda expression
#used to write anonyous function

# def double(x):
#     return x*2

# print(double(5))


#or
'''using lambda function'''

double=lambda x:x*2
cube=lambda x:x*x*x
average=lambda x,y,z:(x+y+z)/3
print(double(5))
print(cube(5))
print(average(3,5,10))



#use lamdba function for one liners
#used when function is passed as one liners

def appl(fx,value):
    return 6+ fx(value)

print(appl(lambda x:x*x*x,2))


'''
Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
'''