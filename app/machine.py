# Import Libraries
import pandas as pd
import numpy as np
from data import Database
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

class Machine:
# Create Model and fit it
    def __init__(self, df):
        self.df = df

# Creates x and y
        target = df["Rarity"]
        features = df.drop(columns="Rarity")

# Creates 3 different models
        self.model1 = RandomForestClassifier()
        self.model2 = LogisticRegression()
        self.model3 = KNeighborsClassifier()

# Trains All The Models
        self.model1.fit(features, target)
        self.model2.fit(features, target)
        self.model3.fit(features, target)

# Gets the prediction for the model
    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        joblib.load(filepath)

    def info(self):
        pass
