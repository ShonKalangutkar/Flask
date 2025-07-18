from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello deviyo sajano app ka swagat hai flask mai"

@app.route("/about")
def about():
    return "this is about us page"

@app.route("/contact")
def contact():
    return "this is a contact page"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You sent some data"
    else:
        return "You are viewing the data"