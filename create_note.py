import requests
from datetime import date

#id and time 
#id --uuid universal unique identifier --> or autocrement 
note_id = input("note_id: ")
title = input("title: ")
body = input("body: ")
today = date.today()
today = today.strftime("%d/%m/%Y")
note = {"id": str(note_id), "title": str(title), "modified" : today, "created": today, "body": str(body)}
new_note = requests.post('http://127.0.0.1:5000/notes', json= note)

print(new_note.status_code)
print(new_note.text)