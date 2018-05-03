import pickle
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from django.conf import settings

class Predictor:
    def __init__(self):
        self.path = "../models/prediction/"
        self.prediction = None
        self.data = None
        self.model = None

    def set_prediction(self, prediction):
        self.prediction = prediction

    def set_data(self, data):
        self.data = data

    def load_model(self, name):
        try:
            path = "api/models/savefile/{}.sav".format(name)
            self.model = pickle.load(open(path, 'rb'))
        except FileNotFoundError:
            self.model = None

    def predict(self):
        try:
            self.check_none()
            if self.prediction == "matakuliah":
                return self.model.predict_proba(self.data), None
            else:
                return None, "prediction is not define"
        except TypeError as error_msg:
            return None, str(error_msg)

    def check_none(self):
        if self.prediction is None:
            raise TypeError("Prediction is None, please set first")
        if self.data is None:
            msg = "Data is None, please check if data is found in models/data or set it first"
            raise TypeError(msg)
        if self.model is None:
            raise TypeError("Model is None, please set first")

def predict_matkul(matkul, data):
    predictor = Predictor()
    predictor.set_prediction("matakuliah")
    predictor.set_data(data)
    predictor.load_model(matkul)

    return predictor.predict()
