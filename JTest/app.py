from flask import Flask
from flask import Blueprint, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)