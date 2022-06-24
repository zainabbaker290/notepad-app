import requests

notes_id = input("enter note id:")

response = requests.get("http://127.0.0.1:5000/notes/" + str(notes_id))

print(response.status_code)
print(response.text)