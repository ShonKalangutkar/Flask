from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    email = db.Column(db.String(200), unique = True)
    posts = db.relationship('POST', backref='author', lazy=True)