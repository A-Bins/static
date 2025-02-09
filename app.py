#!/usr/bin/python3
from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", port=8000)
