# Import Libraries
from data import Database
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import datetime

class Machine:
# Create Model and fit it
    def __init__(self, df):
        self.df = df

        scaler = StandardScaler()

# Creates x and y
        y = df["Rarity"]
        X = df[["Level", "Health", "Energy", "Sanity"]]

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Creates model
        self.RF_model = RandomForestClassifier(n_estimators=100, max_depth=20, n_jobs=-1, random_state=42)

# Trains The Models
        self.RF_model.fit(X_train, y_train)

# Gets the prediction for each model
    def __call__(self, feature_basis):
        return self.RF_model.predict(feature_basis)

# Saves each model to respective filepath
    def save(self, filepath):
        joblib.dump(self.RF_model, "model.joblib")

# Allows user to open specific model
    @staticmethod
    def open(filepath):
        joblib.load(filepath)

# Displays info on each model
    def info(self):
        print("Base Model: Random Forest Classifier")
        print(f"{datetime.datetime.now()}")


db = Database("Monsters").dataframe()
test = Machine(db)
test.info()


"""
I trained 3 different models, RandomForestClassifier, LogisticRegression, and KNeighborsClassifier.
I then tuned each of them using a for loop which changed the parameters for each one and compared the accuracy score.
Upon further analysis i concluded that the RandomForestClassifer was the best model for this project.
It had a 80% accuracy score compared to the 60% from the LogisticRegression and the
72% from the KNeighborsClassifier.
"""