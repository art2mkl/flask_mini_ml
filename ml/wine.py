from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
import os

from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

import joblib
from joblib import dump, load


class Wine :
    def __init__(self):
        # wines = load_wine()
        
        # self.df = pd.DataFrame(data= np.c_[wines['data'], wines['target']],
        #              columns= wines['feature_names'] + ['target'])
        # self.X = self.df.drop('target', axis = 1)
        # self.parameters = [[self.X[i].min(), self.X[i].max(), i] for i in self.X.columns]
        self.fit_model = self.load_model('wine_fit')

    def load_model(self, name):
    #---------------------------------------------------------
        """ • Load model fitted
            • Return Model"""
    #---------------------------------------------------------
    
        the_path = f"{os.path.abspath('')}/static/ml/{name}"
        self.fit_model = load(the_path)
        return self.fit_model

    def predict(self, df):
        prediction = self.fit_model.predict(df)
        return prediction
