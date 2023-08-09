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

# Creates x and y and splits it
        y = df["Rarity"]
        x = df[["Level", "Health", "Energy", "Sanity"]]

        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

# Creates model with best params
        self.RF_model = RandomForestClassifier(n_estimators=100, max_depth=20, n_jobs=-1, random_state=42)

# Trains The Models
        self.RF_model.fit(x_train, y_train)

# Gets the prediction for the model
    def __call__(self, feature_basis):
        return self.RF_model.predict(feature_basis)

# Saves the model
    def save(self, filepath):
        joblib.dump(self.RF_model, "model.joblib")

# Allows user to open model
    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

# Displays info on each model
    def info(self):
        print("Base Model: Random Forest Classifier")
        print(f"Timestamp:", datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))


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