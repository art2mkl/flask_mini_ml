from sklearn.datasets import load_wine
import pandas as pd
import numpy as np

# data = load_wine()
# data.target[[10, 80, 140]]
# array([0, 1, 2])
# list(data.target_names)
# ['class_0', 'class_1', 'class_2']

class Wine :
    def __init__(self):
        wines = load_wine()
        
        self.df = pd.DataFrame(data= np.c_[wines['data'], wines['target']],
                     columns= wines['feature_names'] + ['target'])
    
