##list
#enclosed within aquare bracket
#list can be changed 
marks=[3,5,6,7,8,9,2,10,11,12]
print(marks)
print(type(marks))

##element indexing
print(marks[0])
print(marks[1])
print(marks[2])


#list manipulation
marks.append(66)
print(marks)
#can we add strings or boolean in list(yes)
marks.append("aditya")
marks.append(True)
print(marks)

print(marks[4])


#negative indexing

print(marks[-3])

#always convert negative indexing to positive
print(marks[len(marks)-3])
print(marks[6-3])
print(marks[3])

#suppose u need to find whether a particualr eement is in the list or not
if 7 in marks:
    print("yes")
else:
    print("no") 

if 'aditya' in marks:
    print("yes")
else:
    print("no") 

#same thing applies for string as well       

if "dit" in "aditya":
    print("yes")
else:
    print("no")     

#more indexing

print(marks[1:])
print(marks[:7]) 
print(marks[1:4]) 
print(marks[1::2]) #jump indexing
print(marks[1::3]) #jump indexing              


#list comprehension(creatinga list on the fly)
list=[i*i for i in range(10)]
print(list)

list=[i for i in range(10) if i%2==0]
print(list)