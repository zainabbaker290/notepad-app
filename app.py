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
    
@app.route("/notes/<notes_id>", methods=["GET"])
def get_note(notes_id):
    notes_file = open("notes.json", "r")
    notes_object = json.load(notes_file)
    list_of_notes = notes_object["notes"]
    for note in list_of_notes:
        if note["id"] == str(notes_id):
            notes_file.close()
            return json.dumps(note)
