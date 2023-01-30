#imports and app creation
from multiprocessing import connection
import sqlite3
from flask import Flask
from flask import Blueprint, render_template

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('RealDB.db')
    connection.row_factory = sqlite3.Row #goes through database
    return connection
#routing html pages
@app.route("/")
def home():
    connection = get_db_connection()
    clubs = connection.execute('SELECT * FROM Clubs').fetchall() #selects everything from table
    connection.close()
    return render_template("home.html", clubs=clubs)
@app.route("/profile/<username>")
def profile(username):
    return render_template("home.html", name=username)
@app.route("/templates/ASchoir.html")
def Choir():
    return render_template("ASchoir.html")
@app.route("/templates/art.html")
def Art():
    return render_template("art.html")
@app.route("/templates/BandMP.html")
def BandMP():
    return render_template("BandMP.html")
@app.route("/templates/buddies.html")
def Buddies():
    return render_template("buddies.html")
@app.route("/templates/chess.html")
def Chess():
    return render_template("chess.html")
@app.route("/templates/color.html")
def Color():
    return render_template("color.html")
@app.route("/templates/esports.html")
def eSports():
    return render_template("esports.html")
@app.route("/templates/computer.html")
def Computer():
    return render_template("computer.html")
@app.route("/templates/theatre.html")
def Theatre():
    return render_template("theatre.html")
@app.route("/templates/writingclub.html")
def WritingClub():
    return render_template("writingclub.html")
@app.route("/templates/culinary.html")
def Culinary():
    return render_template("culinary.html")
@app.route("/templates/dance.html")
def Dance():
    return render_template("dance.html")
#running app
if __name__ == '__main__':
    app.run(debug=True)