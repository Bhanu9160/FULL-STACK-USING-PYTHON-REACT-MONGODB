from flask import Flask,render_template,request,redirect,url_for,session 
app = Flask(__name__)
app.secret_key="Bhisaab"
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    session["username"]=username
    return redirect(url_for("dashboard"))
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html",username=session["username"])
    return redirect(url_for("home"))
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("home"))
if __name__ =="__main__":
    app.run(debug=True)