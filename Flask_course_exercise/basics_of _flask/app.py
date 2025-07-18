from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    username= request.form.get("username")
    password= request.form.get("password")
    
    valid_users = {
        'admin':'admin',
        'shon':'1234',
        'aman':'aman',
        'Kanishk':'Kanishk'
    }
    
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name = username)
    else:
        return "Invalid Credentials"