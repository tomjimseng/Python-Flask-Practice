import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/2", {})
print(response.json())

response = request.put(BASE + "video/1", {"name": "Dog", "likes": 20, "views": 100000})
print(response.json())

response = request.put(BASE + "video/3", {"name": "Dog", "likes": 20, "views": 100000})
print(response.json())

response = request.put(BASE + "video/4", {"name": "Dog", "likes": 20, "views": 100000})
print(response.json())

response = request.put(BASE + "video/5", {"name": "Dog", "likes": 20, "views": 100000})
print(response.json())


response = request.get(BASE + "video/1")
print(response.json())