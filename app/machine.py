# Import Libraries
from data import Database
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

class Machine:
# Create Model and fit it
    def __init__(self, df):
        self.df = df

        encoder = LabelEncoder()

# Creates x and y
        self.target = encoder.fit_transform(df["Rarity"])
        self.features = df.drop(columns="Rarity")
        print("Target unique values after label encoding:", set(self.target))
        print("Features information:")
        print(self.features.info())

# Creates 3 different models
        self.RF_model = RandomForestClassifier()
        self.LR_model = LogisticRegression()
        self.KNN_model = KNeighborsClassifier()

# Trains All The Models
        self.RF_model.fit(self.features, self.target)
        self.LR_model.fit(self.features, self.target)
        self.KNN_model.fit(self.features, self.target)

# Gets the prediction for each model
    def __call__(self, feature_basis):
        self.RF_pred = self.RF_model.predict(feature_basis)
        self.LR_pred = self.LR_model.predict(feature_basis)
        self.KNN_pred = self.KNN_model.predict(feature_basis)

# Saves each model to respective filepath
    def save(self, filepath):
        joblib.dump(self.RF_model, "RF_model.joblib")
        joblib.dump(self.LR_model, "LR_model.joblib")
        joblib.dump(self.KNN_model, "KNN_model.joblib")

# Allows user to open specific model
    @staticmethod
    def open(filepath):
        joblib.load(filepath)

# Displays info on each model
    def info(self):
        RF_score = accuracy_score(self.target, self.RF_pred)
        LR_score = accuracy_score(self.target, self.LR_pred)
        KNN_score = accuracy_score(self.target, self.KNN_pred)
        print(RF_score)
        print(LR_score)
        print(KNN_score)

db = Database("Monsters").dataframe()
test = Machine(db)
test.info()
