from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/acerca_de")

def acerca_de():
    return render_template("about.html")

@app.route("/visualizar")

def visualizar():
    return render_template("visualizar.html")
