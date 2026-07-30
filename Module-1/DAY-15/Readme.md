# Day 16 - Flask Redirect & url_for()

## Objective

Learn how to redirect users from one page to another using `redirect()` and generate dynamic URLs using `url_for()`.

---

## Concepts Covered

- redirect()
- url_for()
- Flask Routes
- Page Navigation
- Dynamic URL Generation

---

## Project Structure

```
Day-16/
│── app.py
└── templates/
    ├── home.html
    └── dashboard.html
```

---

## Files Used

- app.py
- templates/home.html
- templates/dashboard.html

---

## Workflow

1. User opens the Home page.
2. User clicks the **Login** link.
3. Flask calls the `/login` route.
4. `redirect(url_for("dashboard"))` redirects the user.
5. Dashboard