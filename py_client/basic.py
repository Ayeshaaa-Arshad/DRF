import requests

# response = requests.get("http://127.0.0.1:8000/api/")
endpoint="http://127.0.0.1:8000/api/"
response = requests.post(endpoint,json={"title":"Dell","description":"This is DELL Laptop","price":"100"})

print(response.json())
