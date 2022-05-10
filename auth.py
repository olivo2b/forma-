from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint("auth", __name__)


@auth.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        name = request.form.get("user_name")
        print(f"{name}")
        return redirect(url_for("views.hello"))

    return render_template("signin.html")


@auth.route("/logout")
def logout():
    return render_template("logout.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nom = request.form.get("user_name")
        email = request.form.get("user_mail")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        print(f"{nom}, {email}, {password}, {password2}")
        if password == password2:
            return redirect(url_for("views.hello"))
    return render_template("login.html")

