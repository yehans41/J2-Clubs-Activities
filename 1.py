'''
from pydoc import render_doc
from flask import Flask, render_template
from views import views
from flask_sqlalchemy import SQLAlchemy
from os import path
# https://www.youtube.com/watch?v=dam0GPOAvVI&t=177s
# https://github.com/yehans41/J2-Clubs-Activities/upload

db = SQLAlchemy()
DB_Name = "database.db"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.config["SECRET KEY"] = "josh chung"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_Name}'
    #db.init_app(app)
    #from models import User, Note
    return app
app = create_app()

def create_database(app):
    if not path.exists('website/' + DB_Name):
        #db.create_all(app)
        print('Created Database!')

create_database(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
# test temporary search bar for fbla-without scanner
'''