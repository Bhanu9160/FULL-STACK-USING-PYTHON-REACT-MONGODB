from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1> Welcome to student Portal</h1>"
@app.route("/student")
def student():
    return """
<h2>Student Details</h2>
Name:Bhanu prakash<br>
College:vvitu<br>
Branch:CSE(cyber security)<br>
"""
@app.route("/skills")
def skills():
    return """ 
<h2>Skils</h2>
Python<br>
splunk<br>
siem<br>
Flask<br>
Cyber security<br>
"""
@app.route("/projects")
def projects():
    return """
<h2>Projects</h2>
Windows login monitoring system<br>
vulnerability assessment usin nessus<br>
"""
@app.route("/contact")
def contact():
    return """ 
<h2>Contact details</h2>
email:battulabhanu569@gmail.com<br>
phone number:8374196170
"""

if __name__ == "__main__":
    app.run(debug=True)