import requests

notes_id = input("enter note id:")

question = input("if you want to update the title please enter title, if the body, please enter body, if both, enter both: ")

if question == "title":
    new_title = input("enter a new title? ")
    result = {"new_body": None, "new_title": new_title}
    response = requests.put("http://127.0.0.1:5000/notes/" + str(notes_id), json = result)
    print(response.status_code)
    print(response.text)
elif question == "body":
    new_body = input("enter a new body? ")
    result = {"new_body": new_body, "new_title": None}
    response = requests.put("http://127.0.0.1:5000/notes/" + str(notes_id), json = result)
    print(response.status_code)
    print(response.text)
elif question == "both":
    new_title = input("enter a new title? ")
    new_body = input("enter a new body? ")
    result = {"new_body": new_body, "new_title": new_title}
    response = requests.put("http://127.0.0.1:5000/notes/" + str(notes_id), json = result)
    print(response.status_code)
    print(response.text)
else: 
    print("you did not choose any of the options")
