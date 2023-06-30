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

    # Connects to Mongo Database
    def __init__(self, uri=getenv("DB_URL"), port=27017, database_name=None):
        self.client = MongoClient(uri, port)
        self.name = database_name

    # Gathers specified number of documents from the Monster library
    def seed(self, amount):
        pass

    # Resets the entire database
    def reset(self):
        self.client.drop_database(self.name)

    # Returns total number of documents in database
    def count(self) -> int:
        pass

    # Creates a dataframe out of entire database
    def dataframe(self) -> DataFrame:
        pass

    # Creates a html table from dataframe, if empty then None
    def html_table(self) -> str:
        pass


db = Database(database_name="Monsters")
db.reset()
