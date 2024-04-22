#code for current time
import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)

if (hour>0 and hour<12):
    print("morning")
elif (hour>12 and hour<17):
    print("afternoon") 
elif (hour>17 and hour<20):
    print("evening") 
else:
    print('night')          

##code for custom hour
import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(input("enter the time hour"))
print(hour)

if (hour>0 and hour<12):
    print("morning")
elif (hour>12 and hour<17):
    print("afternoon") 
elif (hour>17 and hour<20):
    print("evening") 
else:
    print('night')              