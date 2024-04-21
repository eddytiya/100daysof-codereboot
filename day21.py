
#keyword arg
def avg(a, b):
    print("the avg is" , (a+b)/2)
    
avg(4,6)

#default arg
def avg(a=8, b=9):
    print("the avg is" , (a+b)/2)
    
avg()
#or we can change the arg
avg(1,5)
#if we want to change on;y the value of a
avg(2)
#if we want to change only the value of b
avg(b=8)

#required args
def avg(a, b,c=1):
    print("the avg is" , (a+b+c)/2)
    
avg(5,6)
#here we need to provide a,b values and defining value of c os optional



####variable length
def avgs(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("avg is",sum/len(numbers) ) 

avgs(5,6)      