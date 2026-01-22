# Academic Management System (Flask + MySQL)

## 📌 Project Overview

This is a **one-page academic management system** developed using **Flask (Python)** and **MySQL (XAMPP)**.  
The system supports **Admin, Student, and Teacher** roles and performs full **CRUD operations** (Create, Read, Update, Delete) on users.

The project is designed for **academic/university submission** and demonstrates backend development, database connectivity, and role-based routing.

---

## 🚀 Features

- Admin registration and management
- Student registration and login
- Teacher registration and login
- Create, Read, Update, Delete (CRUD) users
- MySQL database integration using XAMPP
- Clean UI with CSS styling
- Flask routing with Jinja2 templates

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Database:** MySQL (phpMyAdmin via XAMPP)
- **IDE:** Visual Studio Code
- **Version Control:** Git & GitHub

---

## 📁 Project Folder Structure

academic_app/
│
├── app.py
├── db.py
├── templates/
│ ├── admin_login.html
│ ├── admin_register.html
│ ├── student_login.html
│ ├── student_register.html
│ ├── teacher_login.html
│ ├── teacher_register.html
│ └── users.html
│
├── static/
│ └── style.css
│
├── venv/
└── README.md

---

## 🔗 Application Routes (URLs)

### Admin

- `/admin/register`
- `/admin/login`

### Student

- `/student/register`
- `/student/login`

### Teacher

- `/teacher/register`
- `/teacher/login`

### CRUD Operations

- `/users` → View all users
- `/users/edit/<id>` → Update user
- `/users/delete/<id>` → Delete user
- `/register` → create users

---

## 🗄 Database Setup (MySQL)

1. Start **XAMPP**
2. Start **Apache** and **MySQL**
3. Open **phpMyAdmin**
4. Create a database:
   ```sql
   CREATE DATABASE academic_db;
   CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(20)
   );
   ```

▶ How to Run the Project

Open the project folder in VS Code

Activate virtual environment:

venv\Scripts\activate

Run Flask app:

python app.py

Open browser:

http://127.0.0.1:8000

📸 Screenshots

🎓 Learning Outcomes

Flask routing and request handling

Database connectivity using MySQL

CRUD operations implementation

MVC-like project structure

GitHub version control

👩‍💻 Developed By

Zuha Junaid
BS Software Engineering

📜 License

This project is for educational purposes only.
