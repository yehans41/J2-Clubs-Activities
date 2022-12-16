#imports and app creation
from flask import Flask
from flask import Blueprint, render_template

app = Flask(__name__)
#routing html pages
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/profile/<username>")
def profile(username):
    return render_template("home.html", name=username)
@app.route("/templates/fbla.html")
def fbla():
    return render_template("fbla.html")
@app.route("/templates/nhs.html")
def nhs():
    return render_template("nhs.html")
@app.route("/templates/scio.html")
def SciO():
    return render_template("scio.html")
#running app
if __name__ == '__main__':
    app.run(debug=True)