from flask import Flask, render_template, request
import generarOnce
import obtenerInformacion
import pandas as pd
import dropbox
import os


app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/acerca_de")

def acerca_de():
    return render_template("about.html")

@app.route("/visualizar")

def visualizar():
    once = generarOnce.generarOnce(7, 7, "3-5-2")
    return render_template("visualizar.html", jornadas=8, once=once)
