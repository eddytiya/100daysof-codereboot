#day96 asyncio

import time

def function1():
    time.sleep(3)
    print("func 1")


def function2():
    time.sleep(3)
    print("func 2")


def function3():
    time.sleep(3)
    print("func 3")       

function3()
function2()
function1()


#THE ABOVE CODE IS NORMALLY DONE BUT WE WILL RUN IT USING ASYNCIO

import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func 1")


async def function2():
    await asyncio.sleep(1)
    print("func 2")


async def function3():
    await asyncio.sleep(4)
    print("func 3") 


async def main():
 L=await asyncio.gather(
     await function1(),
     await function2(),
     await function3()
 ) 


 print(L)    

 asyncio.run(main())



#####some prac code
import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)
   
  return "runnn"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)

async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())