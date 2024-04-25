# #typecasting
# #conversion of one data type to another data type is konown as type casting in python

# a="1"
# b="2"
# print(a+b)#12 cause of string


# a=1
# b=2
# print(a+b)

# #using typecsting
# a="1"
# b="2"
# print(int(a)+int(b))

#types 
#explicit and implicit
#1,explicit:done by user
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

#2.implicit:done by python itself
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))