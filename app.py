from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/notes", methods=["GET"])
def all_notes():
    if request.method == "GET":
        #open python file and read it
        notes_file = open("notes.json", "r")
        #using json loads to read from a string 
        notes_object = json.load(notes_file)
        notes_file.close()
        notes_list = []
        for note in notes_object["notes"]:
            note_result = "[note id: "+  note["id"] + ", note title: " + note["title"] + ", created: " + note["created"] + ", modified: " + note["modified"] + "]"
            notes_list.append(note_result)
        return json.dumps(notes_list)
