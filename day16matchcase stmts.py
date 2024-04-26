#matchcase stmts
#just like switch stmts

x=int(input("enter any number:"))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4") 

    case _ if x!= 90:
        print(f"{x} is not 90") 
    
    case _ if x!= 80:
        print(f"{x} is not 80") 

    
    case _ :
        print(f"{x}")                