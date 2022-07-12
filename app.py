from flask import Flask, request, Response, request_finished
import json
import uuid 
from datetime import date

app = Flask(__name__)

def deserialise_data(file_name):
        notes_file = open(file_name, "r")
        notes_object = json.load(notes_file)
        notes_file.close()
        return notes_object

def get_one_note(notes_id):
        notes_object = deserialise_data("notes.json")
        notes = notes_object.get("notes")
        for key in notes.keys():
            if key == str(notes_id):
                return [notes[key], notes_object]


@app.route("/notes", methods=["GET", "POST"])
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
    
    else:
        Response("method not allowed", status=405)

@app.route("/notes/<notes_id>", methods=["GET", "PUT"])
def get_note(notes_id):

    if request.method == "GET":
                notes_items = get_one_note(notes_id)
                note = notes_items[0]
                return Response(json.dumps(note), status=200)
    
    elif request.method == "PUT":
        notes_item = get_one_note(notes_id)
        note = notes_item[0]
        new_data = request.data
        new_data = json.loads(new_data.decode('utf-8'))
        today = date.today()
        today = today.strftime("%d/%m/%Y")

        if new_data["new_body"] == None:
            note["title"] = new_data["new_title"]
            note["modified"] = today
        
        elif new_data["new_title"] == None:
            note["body"] = new_data["new_body"]
            note["modified"] = today
        
        else:
            note["title"] = new_data["new_title"]
            note["body"] = new_data["new_body"]
            note["modified"] = today

        notes_file = open("notes.json", "w")
        notes_file.write(json.dumps(notes_item[1]))
        notes_file.close()

        return Response(json.dumps(note), status=200)

    return Response("note does not exist", status=404)
        
