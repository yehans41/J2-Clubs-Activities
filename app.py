#imports and app creation
from multiprocessing import connection
import sqlite3
from flask import Flask
from flask import Blueprint, render_template
from flask import Flask,redirect,url_for,render_template,request, jsonify

app = Flask(__name__)
#database connection
def get_db_connection():
    conn = sqlite3.connect('RealDB.db')
    conn.row_factory = sqlite3.Row #goes through database
    return conn
#routing html pages
@app.route("/")
def home():
    conn = get_db_connection()
    #clubs = conn.execute('SELECT * from clubs LEFT JOIN weekdays on clubs.name = weekdays.name').fetchall()
    clubs = conn.execute('SELECT * from clubs').fetchall()
    #weekdays = conn.execute('SELECT * from Weekdays').fetchall()
    conn.close()
    return render_template("home.html", clubs=clubs)
@app.route("/profile/<username>")
@app.route("/templates/base.html")
def base():
    conn = get_db_connection()
    #clubs = conn.execute('SELECT * from clubs LEFT JOIN weekdays on clubs.name = weekdays.name').fetchall()
    clubs = conn.execute('SELECT * from clubs').fetchall()
    #weekdays = conn.execute('SELECT * from Weekdays').fetchall()
    conn.close()
    Name = request.args.get('Name')
    return render_template("base.html", clubs=clubs, Name=Name)
#running app
if __name__ == '__main__':
    app.run(debug=True)