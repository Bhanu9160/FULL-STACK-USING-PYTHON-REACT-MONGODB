from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
    return "Students Result Portal"
@app.route("/student/<name>")
def student(name):
    return f"Welcome{name}"
@app.route("/marks/<int:marks>")
def marks(marks):
    if marks>=35:
        return f"you are passed with {marks} marks"
    else:
        return f"you are failed with {marks} marks"
@app.route("/Details/<name>/<branch>")
def Details(name,branch):
    return f"My name is {name}<br> and Branch name is {branch}"
if __name__ == "__main__":
    app.run(debug=True)