# Day 11 – Static Files in Flask

## Objective

Learn how to use CSS, JavaScript, and Images in a Flask application using the `static` folder.

---

## What are Static Files?

Static files are resources that do not change dynamically when requested by the client. Flask serves these files directly from the `static` folder.

Examples:
- CSS
- JavaScript
- Images
- Icons

---

## Why Use Static Files?

- Improve webpage design using CSS.
- Add interactivity using JavaScript.
- Display images and logos.
- Organize frontend resources in one place.

---

## Project Structure

```
Flask-Day11/
│── app.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
│
└── templates/
    └── home.html
```

---

## HTML Tags Used

### Link CSS

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

Loads the external CSS file.

---

### Display Image

```html
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

Displays an image from the `static/images` folder.

---

### Load JavaScript

```html
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

Loads the external JavaScript file.

---

## Flask Function Used

```python
url_for('static', filename='css/style.css')
```

Generates the correct URL for files stored inside the `static` folder.

---

## Files Created

- app.py
- templates/home.html
- static/css/style.css
- static/js/script.js
- static/images/logo.png

---

## Key Concepts Learned

- Static Folder
- CSS Integration
- JavaScript Integration
- Image Integration
- `url_for()` Function
- External Resource Linking

---

## Learning Outcome

- Created a Flask application with static resources.
- Applied external CSS styling.
- Added JavaScript functionality.
- Displayed images from the static folder.
- Understood how Flask serves static files.

---

## Next Topic

Day 12 – Dynamic URL Parameters