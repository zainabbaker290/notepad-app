import requests

response = requests.get("http://127.0.0.1:5000/notes")

print(response.status_code)
print(response.text)