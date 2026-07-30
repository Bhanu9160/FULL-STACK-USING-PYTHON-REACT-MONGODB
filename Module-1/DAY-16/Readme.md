# Day 16- Flask Sessions

## Objective

Learn how to use Flask Sessions to store user information temporarily after login and remove it during logout.

---

## Concepts Covered

- Flask Session
- session
- app.secret_key
- Login
- Logout
- redirect()
- url_for()
- request.form

---

## Project Structure

```
Day-17/
│── app.py
└── templates/
    ├── index.html
    └── dashboard.html
```

---

## Files Used

- app.py
- templates/index.html
- templates/dashboard.html

---

## Workflow

1. User opens the Login page.
2. User enters a username.
3. Flask receives the username.
4. Username is stored in the session.
5. User is redirected to the Dashboard.
6. Dashboard displays the username.
7. Clicking Logout removes the session.
8. User is redirected back to the Login page.

---

## Routes

```
/
Home (Login Page)

/login
Stores username in session

/dashboard
Displays Dashboard

/logout
Removes session and redirects to Home
```

---

## Commands Used

```python
from flask import session
```

```python
app.secret_key = "bhanu"
```

```python
session["username"] = username
```

```python
session["username"]
```

```python
session.pop("username", None)
```

```python
redirect(url_for("dashboard"))
```

---

## Output

### Login Page

```
Login

Username:
____________

[ Login ]
```

↓

Enter

```
Bhanu
```

↓

### Dashboard

```
Welcome Bhanu

You have successfully logged in.

Logout
```

↓

Click Logout

↓

### Login Page

```
Login

Username:
____________

[ Login ]
```

---

## What I Learned

- Created a login page using Flask.
- Stored user data in a session.
- Displayed session data on another page.
- Used `app.secret_key` to secure sessions.
- Implemented logout using `session.pop()`.
- Redirected users using `redirect()` and `url_for()`.

---


