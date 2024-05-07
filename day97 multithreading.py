#day97 multithreading

#normal
import threading
import time
time1=time.perf_counter()
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
time2=time.perf_counter()
print(time2-time1)
func(4)
func(2)
func(1)    

#we want the 3 funs to run simultaneously so we use threading

#threading
import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()    

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2=time.perf_counter()
print(time2-time1)

#####more advance study

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)



def main():
    time1=time.perf_counter()    
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
     future1 = executor.submit(func,3)
     print(future1.result())
     future2 = executor.submit(func,2)
     print(future2.result())
     future3 = executor.submit(func,4)
     print(future3.result())

poolingDemo()


###using map func

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)



def main():
    time1=time.perf_counter()    
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor as executor:
        l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()
     

