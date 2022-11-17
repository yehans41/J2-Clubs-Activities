'''
from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home.html")


@views.route("/profile/<username>")
def profile(username):
    return render_template("home.html", name=username)

@views.route("/templates/fbla.html")
def fbla():
    return render_template("fbla.html")

@views.route("/templates/nhs.html")
def nhs():
    return render_template("nhs.html")
'''