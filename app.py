from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/notes", methods=["GET"])
def all_notes():
    if request.method == "GET":
        notes_file = open("notes.json", "r")
        notes_object = json.load(notes_file)
        notes_file.close()
        notes_list = []
        for note in notes_object["notes"]:
            note_result = "[note id: "+  note["id"] + ", note title: " + note["title"] + ", created: " + note["created"] + ", modified: " + note["modified"] + "]"
            notes_list.append(note_result)
        return json.dumps(notes_list)

@app.route("/notes/<notes_id>", methods=["GET"])
def get_note(notes_id):
    notes_file = open("notes.json", "r")
    notes_object = json.load(notes_file)
    list_of_notes = notes_object["notes"]
    for note in list_of_notes:
        if note["id"] == str(notes_id):
            notes_file.close()
            return json.dumps(note)
