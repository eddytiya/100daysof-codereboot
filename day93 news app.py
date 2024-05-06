#day93:news app
#api key:6a881dd68dc145528b79a451384b905b

# import requests
# query=input("what kind of news are u interested in:")
# url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-06&sortBy=publishedAt&apiKey=6a881dd68dc145528b79a451384b905b"
# r=requests.get(url)
# print(r.text)

#using above model with json

import requests
import json
query=input("what kind of news are u interested in:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-06&sortBy=publishedAt&apiKey=6a881dd68dc145528b79a451384b905b"
r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------")
    