import requests

notes_id = input("enter note id:")
new_body = input("enter new body: ")

result = {"id": notes_id, "new_body": new_body}

response = requests.put("http://127.0.0.1:5000/notes", json = result)

print(response.status_code)
print(response.text)