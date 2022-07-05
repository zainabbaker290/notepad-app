from flask import Flask, request, Response
import json
import uuid 
from datetime import date

app = Flask(__name__)
#verify legitimate not curropted data
#all notes --> if w/o elife or else bad
#notes methods
#del
#/notes --> change to notes -- update -- create, title body, function return, return response 

#update note next 

def serialise_data(file_name):
        notes_file = open(file_name, "r")
        notes_object = json.load(notes_file)
        notes_file.close()
        return notes_object


@app.route("/notes", methods=["GET", "POST"])
def all_notes():
    if request.method == "GET":
        notes_object = serialise_data("notes.json")
        for note_value in notes_object.values():
            for n_value in note_value.values():
                del n_value["body"]
        
        return json.dumps(notes_object)
    
    elif request.method == "POST":
        notes_object = serialise_data("notes.json")
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
    
@app.route("/notes/<notes_id>", methods=["GET"])
def get_note(notes_id):
    notes_object = serialise_data("notes.json")
    for note in notes_object.values():
        for key in note.keys():
            if key == str(notes_id):
                return json.dumps(note[key])