# Imports Libraries
from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

# Creates Database class
class Database:
    # Loads environmental variables
    load_dotenv()

    # Creates class variable to keep track of all monster entries
    monsters = []

    # Connects to Mongo Database
    def __init__(self, uri=getenv("DB_URL"), port=27017, database_name=None):
        self.client = MongoClient(uri, port)
        self.name = database_name

    # Gathers specified number of documents from the Monster library
    def seed(self, amount):
        for i in range(0, amount):
            self.monsters.append(Monster().to_dict())
        print(self.monsters)
        return self.monsters

    # Resets the entire database
    def reset(self):
        self.client.drop_database(self.name)

    # Returns total number of documents in database
    def count(self) -> int:
        print(len(self.monsters))
        return len(self.monsters)

    # Creates a dataframe out of entire database
    def dataframe(self) -> DataFrame:
        df = DataFrame(self.monsters)
        print(df.head())
        return df

    # Creates a html table from dataframe, if empty then None
    def html_table(self) -> str:
        df = DataFrame(self.monsters)
        if df.empty:
            return None
        else:
            print(df.to_html())

print(Monster())
db = Database("First")
db.seed(amount=5)
db.count()
db.dataframe()
db.html_table()
db.reset()


