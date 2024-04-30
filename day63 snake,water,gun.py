# #day63 snake,water,gun

# #                 S W G
# # computer =      0 1 2
# # player =  S  0  D W L
# #           W  1  L D W
# #           G  2  W L D


# #my logic for snake,water ,gun
# import random

# user=int(input("choose 0 for snake,1 for water and 2 for gun"))
# print(f"you choose {user}")

# computer=random.randint(0,2)
# print(computer)


# if user == computer:
#     print(f"its a draw")
# elif computer >user:
#     print("you win") 
# elif computer <user:
#     print("you lose")    
# else:
#     print("enter a valid input")     
       

#teachers code
import random

def check(comp,user):
    if comp == user:
        return 0
    if (comp==0 and user ==1):
        return -1
    if (comp==1 and user ==2):
        return -1
    if (comp==2 and user ==0):
        return -1
    
    return 1
comp=random.randint(0,2)
user=int(input("choose 0 for snake,1 for water and 2 for gun"))

score =check(comp,user)

print(f"you choose {user}")
print(f"computer choose  {comp}")

if(score == 0):
    print("it is a draw")
elif score==1:
    print("you won")
elif score==-1:
    print("you lose")
else:
    print("enter a correct value")        
