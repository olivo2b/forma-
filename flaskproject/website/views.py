from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/home")
def hello():
    class User:
        def __init__(self):
            self.nom = "dominique"

        def __repr__(self):
            return f"ceci est incroyable"

    dominique = User()
    return render_template("home.html")


@views.route("/contact")
def login():
    return "contact"


@views.route("/apropos")
def apropos():
    return "apropos"
