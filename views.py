
from flask import Flask, render_template, request, url_for
from app import app
from ml.wine import Wine
import pandas as pd

@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html', titre="Home")

@app.route('/test/')
def test():
    return render_template('index.html', titre="Test")

@app.route('/wine/')
def wine():
    
    wine = Wine()
    wine_df = wine.df


    
    

    #return wine.names
    return wine_df.columns

    #return {'a' : 1, 'b' : 2, 'c' : 4}
    
    #render_template('index.html', titre="Wine")


@app.route('/wine2/')
def wine2():
    
    return render_template('wine2.html', info = wine())