
from flask import Flask, render_template, request, url_for
from app import app
from ml.wine import Wine
import pandas as pd
import requests

@app.route('/',methods = ['POST', 'GET'])
@app.route('/home/',methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        alcohol = request.form["alcohol"]
        malic_acid = request.form["malic_acid"]
        ash = request.form["ash"]
        alcalinity_of_ash = request.form["alcalinity_of_ash"]
        magnesium = request.form["magnesium"]
        total_phenols = request.form["total_phenols"]
        flavanoids = request.form["flavanoids"]
        nonflavanoid_phenols = request.form["nonflavanoid_phenols"]
        proanthocyanins = request.form["proanthocyanins"]
        color_intensity = request.form["color_intensity"]
        hue = request.form["hue"]
        od280_od315_of_diluted_wines = request.form["od280_od315_of_diluted_wines"]
        proline = request.form["proline"]

        predict = str(requests.get(url_for(('predict'), 
        alcohol=alcohol,
        malic_acid=malic_acid,
        ash=ash,
        alcalinity_of_ash=alcalinity_of_ash,
        magnesium=magnesium,
        total_phenols=total_phenols,
        flavanoids=flavanoids,
        nonflavanoid_phenols=nonflavanoid_phenols,
        proanthocyanins=proanthocyanins,
        color_intensity=color_intensity,
        hue=hue,
        od280_od315_of_diluted_wines=od280_od315_of_diluted_wines,
        proline=proline,
        _external=True)).text)
        print(predict)
    
    else :
        predict=100

    return render_template('index.html', titre="Home", predict=predict)


@app.route('/predict/')
def predict():
    
    alcohol = request.args.get("alcohol")
    malic_acid = request.args.get("malic_acid")
    ash = request.args.get("ash")
    alcalinity_of_ash = request.args.get("alcalinity_of_ash")
    magnesium = request.args.get("magnesium")
    total_phenols = request.args.get("total_phenols")
    flavanoids = request.args.get("flavanoids")
    nonflavanoid_phenols = request.args.get("nonflavanoid_phenols")
    proanthocyanins = request.args.get("proanthocyanins")
    color_intensity = request.args.get("color_intensity")
    hue = request.args.get("hue")
    od280_od315_of_diluted_wines = request.args.get("od280_od315_of_diluted_wines")
    proline = request.args.get("proline")


    if alcohol != None and malic_acid != None and ash != None and alcalinity_of_ash != None and magnesium != None and total_phenols != None and flavanoids != None and nonflavanoid_phenols != None and proanthocyanins != None and color_intensity != None and hue != None and od280_od315_of_diluted_wines != None and proline != None:
        
        wine = Wine()

        to_predict = pd.DataFrame([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium,
        total_phenols, flavanoids, nonflavanoid_phenols,
        proanthocyanins, color_intensity, hue,
        od280_od315_of_diluted_wines, proline ]])

        prediction = str(wine.predict(to_predict)[0])

    else:
        prediction = "Il manque des paramètres"


    #request = "http://localhost:5000/predict/?alcohol=13.56&malic_acid=1.71&ash=2.31&alcalinity_of_ash=16&magnesium=117.0&total_phenols=3.1&flavanoids=3.29&nonflavanoid_phenols=0.34&proanthocyanins=2.3&color_intensity=6.13&hue=0.95&od280_od315_of_diluted_wines=3.38&proline=795.0"

    return prediction
