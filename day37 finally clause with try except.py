##try...except...finally
def fun1():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error")    
        return 0
    finally:
        print("i m always executed")    

#return aur break functon e bhi farak nhi padta usse
#prodece the errkr by typing letters adsi
x=fun1()
print(x)    