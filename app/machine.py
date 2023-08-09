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

        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

        # Creates x and y and splits it
        y = df["Rarity"]
        x = df[["Level", "Health", "Energy", "Sanity"]]


        # Creates model with best params
        self.RF_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=20,
            n_jobs=-1,
            random_state=42
        )

        # Trains The Models
        self.RF_model.fit(x, y)

    # Gets the prediction for the model
    def __call__(self, feature_basis):
        prediction, *_ = self.RF_model.predict(feature_basis)
        confidence, *_ = self.RF_model.predict_proba(feature_basis)
        return prediction, max(confidence)

    # Saves the model
    def save(self, filepath):
        joblib.dump(self.RF_model, "model.joblib")

    # Allows user to open model
    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    # Displays info on each model
    def info(self):
        return f"Base Model: Random Forest Classifier<br>Timestamp: {self.timestamp}"


if __name__ == '__main__':
    df = Database("Monsters").dataframe()
    machine = Machine(df)
    print(machine)

"""
I trained 3 different models, RandomForestClassifier,
LogisticRegression, and KNeighborsClassifier.

I then tuned each of them using a for loop which changed
the parameters for each one and compared the accuracy score.

Upon further analysis i concluded that the RandomForestClassifer
was the best model for this project.

It had a 80% accuracy score compared to the 60% from the LogisticRegression and the
72% from the KNeighborsClassifier.
"""
