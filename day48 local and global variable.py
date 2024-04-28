#local and global variable
x=4
print(x)


def hello():
    x=5
    print(f"the local x is {x}")
    print("hello adi")

print(f"the global x is {x}")
hello()
print(f"the global x is {x}")

#suppose u want your global variable to change from 4 to 5
#what u will do in hello to do that

#local variable :in a function and can be accessed in a function only
#global variable:can be accessed outside or within a function



####consider this example
x = 10 # global variable

def my_function():
  global x#this keyword wil cahnge the global variable with local value
  x=4
  y = 5 # local variable
  print(y)

my_function()
print(x)
#print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
