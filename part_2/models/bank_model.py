from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = "Banks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)