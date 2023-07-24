from flask import render_template, request
from app import app
from .controllers.controller import generate_random_password


@app.route("/")
def home():
    return render_template("index.html")

# Нужна помощь в реализации редиректа в функции
@app.route("/generate", methods=["POST"])
def generate_password():
    length = int(request.form["length"])
    password = generate_random_password(length)
    return render_template("index.html", password=password)
