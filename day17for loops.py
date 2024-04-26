# ##for loops

# #printing numbers from ito 20000
# for i in range(1,20000):
#     print(i+1)


# #odd numbers

# number=int(input("number:"))

# for i in range(1,number,2):
#     print(i)    

# #even numbers

# number=int(input("number:"))

# for i in range(1,number,2):
#     print(i+1)   

# #tables
# number=int(input("number:"))

# for i in range(1,11):
#     print(number,"x",i,"=",number*i)

# #pyramid

# rows=int(input("enter the number of rows:"))

# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

#     i-=1    

# #strings
# name = "abhishek"

# for i in name:
#     print(i)
#     if(i=='i'):
#         print("iiooo")

colors=["red","blue","green","yellow"]

for color in colors:
    print(color)