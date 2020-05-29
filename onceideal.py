from flask import Flask, render_template, request
import generarOnce
import obtenerInformacion
import pandas as pd
import dropbox
import os

equipos = [1, 2, 3, 4, 5, 6, 7, 10, 13, 16, 17, 18]
#Lista de todos los de primera división [1, 2, 3, 4, 5, 6, 7, 10, 13, 16, 17, 18]

jornadas = []
for i in range(16, 19):
    jornadas.append(i)

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/acerca_de")

def acerca_de():
    return render_template("about.html")

@app.route("/visualizar")

def visualizar():
    once = generarOnce.generarOnce(jornadas, equipos, "3-4-3")
    return render_template("visualizar.html", jornadas=8, once=once)
