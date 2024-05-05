#walrus operator
'''
The Walrus Operator is represented by the := syntax 
and can be used in a variety of contexts including 
while loops and if statements.

walrus operator assigns value too a variable as a result to another variable

'''


# a=True
# print(a:=False)

#using walrus operator in while loops
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())


# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy)

print(happy := True)

foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
          break
  foods.append(food)

#or

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)