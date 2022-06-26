from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/notes", methods=["GET", "POST"])
def all_notes():
    if request.method == "GET":
        notes_file = open("notes.json", "r")
        notes_object = json.load(notes_file)
        notes_file.close()
        for note in notes_object["notes"]:
            note.pop("body")
        return json.dumps(notes_object)
    
    if request.method == "POST":
        notes_file = open("notes.json", "r")
        notes_object = json.load(notes_file)
        data = request.json
        notes_object["notes"].append(data)
        notes_file.close()
        notes_file = open("notes.json", "w")
        notes_file.write(json.dumps(notes_object))
        notes_file.close()
        return Response(json.dumps(data), status=201)
    
@app.route("/notes/<notes_id>", methods=["GET"])
def get_note(notes_id):
    notes_file = open("notes.json", "r")
    notes_object = json.load(notes_file)
    list_of_notes = notes_object["notes"]
    for note in list_of_notes:
        if note["id"] == str(notes_id):
            notes_file.close()
            return json.dumps(note)
