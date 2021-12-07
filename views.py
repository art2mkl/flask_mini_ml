
from flask import Flask, render_template
from app import app
from ml.wine import Wine

@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html', titre="Home")

@app.route('/test/')
def test():
    return render_template('index.html', titre="Test")

@app.route('/wine/')
def wine():
    vin = Wine()

    return render_template('index.html', titre="Wine")
