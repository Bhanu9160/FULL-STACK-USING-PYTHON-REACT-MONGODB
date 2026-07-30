from flask import Flask,render_template,request 
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    timestamp = datetime.now()
    return render_template("index.html",timestamp=timestamp)
@app.route("/submit",methods=["POST"])
def submit():
    username = request.form["username"]
    email = request.form["email"]
    roll = request.form["roll"]
    return render_template("output.html",username=username,email=email,roll=roll)
if __name__=="__main__":
    app.run(debug=True)