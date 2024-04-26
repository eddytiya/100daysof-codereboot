#ennumerate function

marks=[12,56,98,12,45,1,4]

index=0
for mark in marks:
    print(mark)
    if (index==2):
        print("harry is awesome")
    index+=1    

#ennumerate function is used to reduce the abobe steps    

marks=[12,56,98,12,45,1,4]

index=0
for index,mark in enumerate(marks) :
    print(mark)
    if (index==2):
        print("harry is awesome")
    index+=1    

#more examples

#print the indexes along with fruit list
fruits=["apple","banana","cherry"]

for index,f in enumerate(fruits):
    print(index,f)

#when u want to start the index from 1 
fruits=["apple","banana","cherry"] 

for index,f in enumerate(fruits,start=1):
    print(index,f)
