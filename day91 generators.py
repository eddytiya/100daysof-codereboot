#day91:generators
'''
you can create a generator by using the yield statement in a function.
The yield statement returns a value from the generator and suspends 
the execution of the function until the next value is requested.
'''

def my_generator():
    for i in range(5):
        yield i

gen=my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
       #OR
for j in gen:
    print(j)

