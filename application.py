from flask import Flask, render_template, session, request
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route('/', methods=["POST", "GET"])
def index():
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("notes")
        session["notes"].append(note)

    return render_template('index.html', notes=session["notes"])

@app.route('/todo-app', methods=["POST", "GET"])
def todo():
    return render_template('todo.html')
