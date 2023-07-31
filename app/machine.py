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
        self.RF_model = RandomForestClassifier()
        self.LR_model = LogisticRegression()
        self.KNN_model = KNeighborsClassifier()

# Trains All The Models
        self.RF_model.fit(features, target)
        self.LR_model.fit(features, target)
        self.KNN_model.fit(features, target)

# Gets the prediction for each model
    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)

# Saves each model to respective filepath
    def save(self, filepath):
        joblib.dump(self.RF_model, "RF_model.joblib")
        joblib.dump(self.LR_model, "LR_model.joblib")
        joblib.dump(self.KNN_model, "KNN_model.joblib")

# Allows user to open specific model
    @staticmethod
    def open(filepath):
        joblib.load(filepath)

# Displays info on
    def info(self):
        pass
