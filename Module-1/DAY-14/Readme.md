# Day 15 - Flask GET Method

## Objective
Learn how to send data from an HTML form to a Flask application using the GET method and retrieve the submitted data using `request.args`.

---

## Concepts Covered

- HTML Forms
- GET Method
- request.args.get()
- URL Parameters
- Form Submission
- Input Validation using `required`

---

## Project Structure

```
Day-15/
│── app.py
└── templates/
    └── index.html
```

---

## Files Used

- app.py
- templates/index.html

---

## Workflow

1. User opens the home page.
2. User enters a username.
3. User clicks the **Search** button.
4. The browser sends the data using the GET method.
5. Flask receives the data using `request.args.get()`.
6. The entered username is displayed on the screen.

---

## URL Example

```
http://127.0.0.1:5000/search?username=Bhanu
```

---

## Output

```
Search User

Username: Bhanu

[Search]

------------------

Welcome Bhanu
```

---

## Commands Used

```python
request.args.get("username")
```

```html
<form action="/search" method="GET">
```

---

## Key Difference

| GET | POST |
|------|------|
| Data is visible in the URL | Data is hidden from the URL |
| Uses request.args | Uses request.form |
| Used for searching | Used for login and registration |

---

## What I Learned

- Created an HTML form.
- Used the GET method.
- Retrieved form data using `request.args.get()`.
- Understood how GET requests work.
- Learned why the `required` attribute is used in HTML forms.

---

