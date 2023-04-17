#imports and app creation
from multiprocessing import connection
from google.oauth2.service_account import Credentials
import os
import json
import gspread
import sqlite3
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask
from flask import Blueprint, render_template
from flask import Flask,redirect,url_for,render_template,request, jsonify

"""
file_path = 'C:/Users/yehan.s.subasinghe/Desktop/J2-Clubs-Activities/credentials.json'
print(os.path.exists(file_path))
with open('C:/Users/yehan.s.subasinghe/Desktop/J2-Clubs-Activities/credentials.json') as f:
    creds_dict = json.load(f)
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = Credentials.from_service_account_file('C:/Users/yehan.s.subasinghe/Desktop/J2-Clubs-Activities/credentials.json', scope=scope)
client = gspread.authorize(creds)
sheet = client.open('J2 Clubs Spreadsheet').sheet1
data = sheet.get_all_values()
conn = sqlite3.connect('RealDB.db')
c = conn.cursor()
for row in data:
    name = row['Name']
    value = row['Value']
    c.execute("SELECT * FROM clubs WHERE name=?", (name,))
    if c.fetchone() is None:
        # Record does not exist, insert new record
        c.execute("INSERT INTO clubs (name, value) VALUES (?, ?)", (name, value))
    else:
        # Record exists, update value
        c.execute("UPDATE clubs SET value=? WHERE name=?", (value, name))
conn.commit()
conn.close()
"""
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
    clubs = conn.execute('SELECT * from clubs LEFT JOIN weekdays on clubs.name = weekdays.name').fetchall()
    conn.close()
    return render_template("home.html", clubs=clubs)
@app.route("/profile/<username>")
@app.route("/templates/base.html")
def base():
    conn = get_db_connection()
    clubs = conn.execute('SELECT * from clubs LEFT JOIN weekdays on clubs.name = weekdays.name').fetchall()
    conn.close()
    Name = request.args.get('Name')
    return render_template("base.html", clubs=clubs, Name=Name)
#running app
if __name__ == '__main__':
    app.run(debug=True)