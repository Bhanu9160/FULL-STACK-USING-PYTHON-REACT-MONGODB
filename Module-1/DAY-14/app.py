from flask import Flask,render_template,request 
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    timestamp = datetime.now()
    return render_template("index.html",timestamp=timestamp)
@app.route("/search",methods=["GET"])
def search():
    username = request.args.get("username")
    if username:
        return f"<h2>Welcome {username}</h2>"
    else:
        return f"<h2>Please enter a username</h2>"
if __name__ == "__main__":
    app.run(debug=True)
