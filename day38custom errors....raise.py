#custom errors.....raise keyword

#used to stop program and not raise further complications

a=int(input("enter any value:"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

