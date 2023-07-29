# Import Libraries
import pandas as pd
import numpy as np
from data import Database
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

class Machine:
# Create Model and fit it
    def __init__(self, df):
        self.df = df
        target = df["Rarity"]
        features = df.drop(columns="Rarity")
        self.model =
        self.model.fit(features, target)

# Gets the prediction for the model
    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)

    def save(self, filepath):
        pass

    @staticmethod
    def open(filepath):
        pass

    def info(self):
        pass
