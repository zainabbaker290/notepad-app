import requests

title = input("title: ")
body = input("body: ")
note = {"title": str(title), "body": str(body)}
new_note = requests.post('http://127.0.0.1:5000/notes', json = note)

print(new_note.status_code)
print(new_note.text)