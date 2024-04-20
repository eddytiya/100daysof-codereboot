# a=10
# b=5
# gmean=(a*b)/(a+b)
# print(gmean)

# c=8
# d=7

# gmean2=(c*d)/(c+d)
# print(gmean2)



###the above code is repeatative for findin g mean instead we can use a funcetion to define the gmaen

def mean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

    if (a>b):
        print("first number is greater")
    else:
        print("second number is greater")    


a=int(input("enter the number for a:"))
b=int(input("enter the number for b:"))

mean(a,b)


##we can change the number as well if we want for oother varibles

c=10
d=7
mean(c,d)
