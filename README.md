<img width="1919" height="966" alt="Screenshot 2026-01-22 221757" src="https://github.com/user-attachments/assets/5659f87b-9797-4521-955a-0d36f270db86" /># Academic Management System (Flask + MySQL)

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
<img width="371" height="610" alt="Screenshot 2026-01-22 221613" src="https://github.com/user-attachments/assets/a4cb93ff-6181-4279-a528-06a7660a4c70" />
<img width="1919" height="965" alt="Screenshot 2026-01-22 221845" src="https://github.com/user-attachments/assets/b975dec2-c3e8-438d-82a0-e372c7372502" />
<img width="1919" height="967" alt="Screenshot 2026-01-22 221249" src="https://github.com/user-attachments/assets/54d8da7a-d318-41e1-8bf2-b0a3717e7420" />
<img width="1918" height="967" alt="Screenshot 2026-01-22 221317" src="https://github.com/user-attachments/assets/f3f48b8a-0eb2-4d2e-996a-e42a1ee0b00f" />
<img width="1919" height="966" alt="Screenshot 2026-01-22 221757" src="https://github.com/user-attachments/assets/b9461490-70c3-4b54-a9c2-d42c8d031fbd" />
<img width="1917" height="968" alt="Screenshot 2026-01-22 221354" src="https://github.com/user-attachments/assets/32d98b92-ede1-40dd-8ee2-7d865168ff04" />
![Uploading Screenshot 2026-01-22 221757.png…]()
<img width="1913" height="965" alt="Screenshot 2026-01-22 221221" src="https://github.com/user-attachments/assets/29a7ed3f-5edb-482f-9157-f6b719f0f3cf" />

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

