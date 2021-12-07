from flask import Flask
from config import Configuration
import os

os.system('export FLASK_ENV=development')

app = Flask(__name__)
app.config.from_object(Configuration)


# from sklearn.datasets import load_wine
# data = load_wine()
# data.target[[10, 80, 140]]
# array([0, 1, 2])
# list(data.target_names)
# ['class_0', 'class_1', 'class_2']

