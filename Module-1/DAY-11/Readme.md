Day 9 – Flask Template Inheritance

Objective

Learn how to create a common layout for multiple web pages using Jinja2 Template Inheritance.

---

What is Template Inheritance?

Template Inheritance is a Jinja2 feature that allows multiple HTML pages to share a common layout. Instead of writing the same HTML code (header, navigation bar, footer) on every page, we create a single "base.html" file and let other pages inherit it.

---

Why Use Template Inheritance?

- Avoids duplicate code.
- Makes the application easier to maintain.
- Provides a consistent layout across all pages.
- Updating "base.html" automatically updates every page.

---

Jinja2 Syntax

Extends

{% extends "base.html" %}

Inherits the parent template.

---

Block

{% block content %}
{% endblock %}

Creates a section that child templates can replace.

---

Project Structure

Flask-Day9/
│── app.py
│
└── templates/
    ├── base.html
    ├── home.html
    ├── about.html
    ├── contact.html
    └── dashboard.html

---

Workflow

1. Create "base.html".
2. Add common HTML elements.
3. Define a content block.
4. Create child templates.
5. Use "extends" to inherit the base template.
6. Replace the content block with page-specific content.

---

Key Concepts Learned

- "extends"
- "block"
- "endblock"
- Reusable layouts
- Template inheritance
- Common navigation and footer

---

Files Created

- "app.py"
- "base.html"
- "home.html"
- "about.html"
- "contact.html"
- "dashboard.html"

---

Outcome

Successfully built a Flask application using Template Inheritance, where all pages share the same layout while displaying different content.