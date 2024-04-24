#for loops with else
#else block can be use also in while loops
#else block is indicated for end of loop

for i in range(5):
    print(i+1)
else:
    print("sorry out of range") 

##when loops is break most of time else does not gets executed
for i in range(5):
    print(i+1)
    if i==4:
        break
else:
    print("sorry out of range")    

#while
i=0

while i<6:
    print(i)
    i+=1
else:
    print("end of loop")


i=0

while i<6:
    print(i)
    i+=1
    if i==4:
        break
else:
    print("end of loop")        
