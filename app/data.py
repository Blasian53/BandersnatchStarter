# Imports Libraries
from os import getenv
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from certifi import where


# Creates Database class
class Database:
    # Loads environmental variables
    load_dotenv()

    # Creates class variable to keep track of all monster entries
    monsters = []

    # Creates collection
    def __init__(self, uri=getenv("DB_URL")):
        self.database = MongoClient(uri, tlsCAFile=where())["Labs"]

    # Gathers specified number of documents from the Monster library
    def seed(self, amount):
        for i in range(0, amount):
            self.monsters.append(Monster().to_dict())
        return self.monsters

    # Resets the entire database
    def reset(self):
        self.monsters = []

    # Returns total number of documents in database
    def count(self) -> int:
        return len(self.monsters)

    # Creates a dataframe out of entire database
    def dataframe(self) -> DataFrame:
        df = DataFrame(self.monsters)
        return df

    # Creates a html table from dataframe, if empty then None
    def html_table(self) -> str:
        df = DataFrame(self.monsters)
        if df.empty:
            return None
        else:
            return df.to_html()


# Calls Database and fills it with 1500 random monsters
db = Database()
db.seed(amount=1500)
