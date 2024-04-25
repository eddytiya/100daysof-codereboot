#if...else
no1=int(input("enter the no1:"))
no2=int(input("enter the no2:"))

operator=input("enter the operator + - * / :")

ans=0

if operator == '+':
    ans=no1+no2
    print(ans)
elif operator == '-':
    ans=no1-no2
    print(ans)
elif operator == '*':
    ans=no1*no2
    print(ans)
elif operator == '/':
    ans=no1/no2
    print(ans)
else:
    print("error")

