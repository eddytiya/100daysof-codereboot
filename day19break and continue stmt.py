#break and continue stmt
#break stmt terminates the loop

for i in range(120):
    print("5 X",i+1,"=",5*(i+1))
    if i==10:
        break

print("loop ko chodkar likal gaya")


#table what i do
num=int(input("enter the number"))

for i in range(1,11):
    print(num,"x",i,"=",num*i)

#pyramid

rows=int(input("enter the number of rows:"))

for i in range(0,rows,1):
    for j in range(i+1):
        print("*",end=" ")
    print()    

#continue
for i in range(12):
    if (i==10):
        print("skips the curent iteration(10 here) and continues to loop thru")
        continue
    print("5 X",i,"=",5*(i))
    

#implementing do while loop in python(infiinte while)

i=0
while True:
    print(i+1)
    i=i+1
    if (i%100 == 0):
        break