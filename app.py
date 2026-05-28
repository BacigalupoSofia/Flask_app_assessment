from flask import Flask, render_template, request, redirect, url_for|
from data_base import products


app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')