# Intern_Dashboard_Task
# Intern Dashboard Project

A simple Django-based Intern Dashboard application that allows adding new interns and displaying them in a list.

## Features

* Dashboard page displaying a list of interns.
* Add New Intern form (Name, Role, Email).
* Data stored in SQLite database.
* Simple frontend styling using CSS.

## Project Structure

```
intern_dashboard_project/
├── dashboard/
│   ├── migrations/
│   ├── static/
│   │   └── dashboard/
│   │       └── style.css
│   ├── templates/
│   │   └── dashboard/
│   │       ├── dashboard.html
│   │       └── add_intern.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── intern_dashboard/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/intern_dashboard_project.git
   cd intern_dashboard_project
   ```

2. **Create Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install django
   ```

4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Screenshots

(Add screenshots of your Dashboard Page and Add Intern Page here)

## Tech Stack

* Python 3.x
* Django 5.x
* SQLite3
* HTML/CSS (basic frontend)

## Note

This project currently supports **Add Intern functionality** only. (No Delete/Edit functionalities are implemented as per the assignment instructions.)

## Author

* [Bhavya Reddy](https://github.com/BhaviReddyy)





Do you want me to generate this README.md as a **ready-to-upload file (.md)?**
