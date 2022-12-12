from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class MyModel(db.Model):
    __tablename__ = 'mymodel'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))

db.create_all()