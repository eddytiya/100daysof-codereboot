#tuples
#unchangable
#round brackets
#can have strings bool values as well
tup=(1,5,4,5,6,7,8,9,'aditya',True)

print(type(tup),tup)#multiple variables to be priented
print(tup)

print(tup[0])
print(tup[2])
print(tup[5])


if 3421 in tup:
    print("yes")
else :
    print("no")    


#slicing
tup2= tup[1:4]
print(tup2)    