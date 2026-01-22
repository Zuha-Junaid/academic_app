from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return "<h2>Academic App Running</h2><a href='/users'>View Users</a>"


# ---------------- READ USERS ----------------
@app.route('/users')
def users():
    con = get_db_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    con.close()
    return render_template('users.html', users=data)


# ---------------- ADMIN REGISTER (CREATE) ----------------
@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        con = get_db_connection()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s,%s,%s,'admin')",
            (
                request.form['name'],
                request.form['email'],
                request.form['password']
            )
        )
        con.commit()
        con.close()
        return redirect(url_for('users'))

    return render_template('admin_register.html')
# ---------------- ADMIN LOGIN ----------------
@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        return redirect('/users')   # temporary success
    return render_template('admin_login.html')


# ---------------- STUDENT REGISTER (CREATE) ----------------
@app.route('/student/register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        con = get_db_connection()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s,%s,%s,'student')",
            (
                request.form['name'],
                request.form['email'],
                request.form['password']
            )
        )
        con.commit()
        con.close()
        return redirect(url_for('users'))

    return render_template('student_register.html')
# ---------------- STUDENT LOGIN ----------------
@app.route('/student/login', methods=['GET','POST'])
def student_login():
    if request.method == 'POST':
        return redirect('/')
    return render_template('student_login.html')


# ---------------- TEACHER REGISTER (CREATE) ----------------
@app.route('/teacher/register', methods=['GET', 'POST'])
def teacher_register():
    if request.method == 'POST':
        con = get_db_connection()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s,%s,%s,'teacher')",
            (
                request.form['name'],
                request.form['email'],
                request.form['password']
            )
        )
        con.commit()
        con.close()
        return redirect(url_for('users'))

    return render_template('teacher_register.html')
# ---------------- TEACHER LOGIN ----------------
@app.route('/teacher/login', methods=['GET','POST'])
def teacher_login():
    if request.method == 'POST':
        return redirect('/')
    return render_template('teacher_login.html')


# ---------------- UPDATE USER ----------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    if request.method == 'POST':
        cur.execute(
            "UPDATE users SET name=%s, email=%s, role=%s WHERE id=%s",
            (
                request.form['name'],
                request.form['email'],
                request.form['role'],
                id
            )
        )
        con.commit()
        con.close()
        return redirect(url_for('users'))

    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cur.fetchone()
    con.close()
    return render_template('update.html', user=user)


# ---------------- DELETE USER ----------------
@app.route('/delete/<int:id>')
def delete_user(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    con.commit()
    con.close()
    return redirect(url_for('users'))


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True, port=8000)
