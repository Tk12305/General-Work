import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()
print(data)  # {"userid : 1, "title": "---", "complete": false}