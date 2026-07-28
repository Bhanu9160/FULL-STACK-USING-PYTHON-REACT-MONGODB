# Day 10 — Flask Forms, User Input & Security Testing

## Objective
Learn how to collect user input using HTML forms and process it in Flask, then apply basic web reconnaissance and penetration-testing tools against the running application to understand how it appears from an attacker's perspective.

---

## Part 1: Flask Forms and User Input

### Topics Covered
- Flask Routing
- HTML Forms
- POST Method
- request.form
- render_template()
- Passing data from Flask to HTML using Jinja2

### How It Works
1. User opens the home page.
2. index.html displays a form.
3. User enters their name.
4. Clicking Submit sends the data using the POST method.
5. Flask receives the data using request.form.
6. The name is passed to Result.html and rendered back to the user.

### Technologies Used
- Python
- Flask
- HTML
- Jinja2

### Concepts Learned
- Flask routing (@app.route)
- HTML forms and form submission
- POST requests
- request.form for reading form data
- Jinja2 template engine
- Passing variables from Python to HTML

### Output
- Home page with a user input form
- Welcome page displaying the entered name

---

## Part 2: Mini Project — Web Enumeration & Penetration Testing

As a follow-up, the running Flask app (http://127.0.0.1:5000) was used as a target to practice basic web reconnaissance and enumeration techniques using common security testing tools.

### Tools Used
- WhatWeb — fingerprinting the web server/framework
- cURL — inspecting raw HTTP requests/responses
- Wget — retrieving pages and testing accessibility
- Gobuster — directory/endpoint brute-forcing
- Dirb — directory brute-forcing (cross-check against Gobuster)

### Target
http://127.0.0.1:5000

### Observations
- Server detected: (fill in from whatweb output)
- Framework: Flask
- Python version: (fill in from whatweb output)
- Directories found: (fill in from gobuster/dirb output)

### Key Findings
- The application only exposes two real routes: / (GET) and /submit (POST). Enumeration tools returned mostly 404 Not Found for guessed paths.
- Accessing /submit with GET instead of POST returns 405 Method Not Allowed, confirming the route is POST-only.
- app.run(..., debug=True) is enabled in App.py. This is fine for local development but should never be used in production, since Flask's debug mode can expose the interactive Werkzeug debugger (and a remote code execution risk) if an unhandled exception occurs.

### Screenshots
- WhatWeb: Screenshots/01_whatweb.png
- cURL: Screenshots/02_curl.png
- Wget: Screenshots/03_wget.png, Screenshots/04_wget.png
- Gobuster: Screenshots/05_gobuster.png
- Dirb: Screenshots/06_dirb.png
- Notes: Screenshots/Notes.png

---

## Overall Takeaways
- Built a simple full-stack form flow using Flask + Jinja2.
- Practiced reconnaissance/enumeration tools against a self-hosted target in a safe, legal environment.
- Learned to spot a real security misconfiguration (debug=True) through hands-on testing rather than just reading about it.