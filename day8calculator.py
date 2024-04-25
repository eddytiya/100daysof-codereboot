#calculator

number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))

operator=input("enter the operation ypu want to perform(+,-,*,/,//,**,%):")

if operator == "+":
    add=number1+number2
    print(f"the addition of {number1} and {number2} is: {add}:")

elif operator == "-":
    subtraction=number1-number2
    print(f"the subtraction of {number1} and {number2} is: {subtraction}:") 
elif operator == "*":
    mul=number1*number2
    print(f"the multiplication of {number1} and {number2} is: {mul}:")
elif operator == "/":
    div=number1/number2
    print(f"the division of {number1} and {number2} is: {div}:")           
elif operator == "//":
    floordiv=number1//number2
    print(f"the floor division of {number1} and {number2} is: {floordiv}:")
elif operator == "%":
    mod=number1%number2
    print(f"the subtraction of {number1} and {number2} is: {mod}:") 
elif operator == "**":
    expo=number1**number2
    print(f"the exponential of {number1} and {number2} is: {expo}:")
else:
    print("invalid operation")    
