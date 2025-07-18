from flask import Flask, redirect, render_template, request, flash, get_flashed_messages, url_for
from form import RegistrationFrom

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}! You have registered Succsefully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form = form)

@app.route("/sucess")
def success():
    return render_template("sucess.html")
        