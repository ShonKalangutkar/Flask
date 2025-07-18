from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def login_form():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == 'admin' and password == '1234':
        return redirect(url_for('student_profile'))
    else:
        return 'Invalid Credentials'

@app.route("/profile")
def student_profile():
    return render_template("profile.html",
                           name="Arun",
                           is_topper=True,
                           subjects=["Maths", "Science", "History"])
