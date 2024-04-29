#map,filter and reduce

'''
map
'''

def cube(x):
    return(x*x*x)

print(cube(2))

# l=[1,2,4,6,4,3]
# newl=[]

# for item in l:
#     newl.append(cube(item))

# print(newl)

#SHORTCUT TRICK FOR ABOVE CODE

l=[1,2,4,6,4,3]
newl=[]
newl=list(map(cube,l))
print(newl)


#FILTER
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)
# Print the even numbers
print(list(evens))

#REDUCE
from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)