#day89:exercise 9
#request module

# #GET requests:this request gives us the code of a requested webite
# import requests

# response=requests.get("https://www.google.com/")
# print(response.text)

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'aditya',
    "body": 'ban rahi hai',
    "userId":1,
}

headers =  {
     'Content-type': 'application/json; charset=UTF-8',
   }

response = requests.post(url, headers=headers, json=data)

print(response.text)