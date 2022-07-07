from flask import Flask, request, Response
import json
import uuid 
from datetime import date

app = Flask(__name__)

def deserialise_data(file_name):
        notes_file = open(file_name, "r")
        notes_object = json.load(notes_file)
        notes_file.close()
        return notes_object

@app.route("/notes", methods=["GET", "POST", "PUT"])
def all_notes():
    if request.method == "GET":
        notes_object = deserialise_data("notes.json")
        notes = notes_object.get("notes")

        for value in notes.values():
            del value["body"]
        
        return Response(json.dumps(notes_object), status=200)

    elif request.method == "POST":
        notes_object = deserialise_data("notes.json")
        data = request.json
        #using uuid4 creates random uuid 
        note_id = uuid.uuid4()
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        data["created"] = today
        data["modified"] = today 
        notes_object[str(note_id)] = data
        
        notes_file = open("notes.json", "w")
        notes_file.write(json.dumps(notes_object))
        notes_file.close()

        return Response(json.dumps(data), status=201)
    
    elif request.method == "PUT":
        notes_object = deserialise_data("notes.json")
        new_data = request.data
        new_data = json.loads(new_data.decode('utf-8'))
        notes = notes_object.get("notes")
        today = date.today()
        today = today.strftime("%d/%m/%Y")

        for key in notes.keys():
            if key == new_data["id"]:
                needed_note = notes[key]
                needed_note["body"] = new_data["new_body"]
                needed_note["modified"] = today

                notes_file = open("notes.json", "w")
                notes_file.write(json.dumps(notes_object))
                notes_file.close()
                return Response(json.dumps(notes[key]), status=200)

        return Response("note does not exist", status=404)
    
    else:
        Response("method not allowed", status=405)

@app.route("/notes/<notes_id>", methods=["GET"])
def get_note(notes_id):
    notes_object = deserialise_data("notes.json")

    notes = notes_object.get("notes")
    for key in notes.keys():
        if key == str(notes_id):
            return Response(json.dumps(notes[key]), status=200)
        
    return Response("note does not exist", status=404)