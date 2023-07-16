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
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Labs"]

    # Creates collection
    def __init__(self, collection: str):
        self.collection = self.database[collection]

    # Gathers specified number of documents from the Monster library
    def seed(self, amount):
        # Creates class variable to keep track of all monster entries
        monsters = []
        for i in range(0, amount):
            monsters.append(Monster().to_dict())
        self.collection.insert_many(monsters)

    # Resets the entire database
    def reset(self):
        self.collection.delete_many({})

    # Returns total number of documents in database
    def count(self) -> int:
        return self.collection.count_documents({})

    # Creates a dataframe out of entire database
    def dataframe(self) -> DataFrame:
        df = DataFrame(self.collection.find({},{"_id":False}))
        return df

    # Creates a html table from dataframe, if empty then None
    def html_table(self) -> str:
        df = self.dataframe()
        if df.empty:
            return None
        else:
            return df.to_html()


if __name__ == '__main__':

# Calls Database and fills it with 1500 random monsters
    db = Database("Monsters")
    db.reset()
    db.seed(amount=1500)
    print(db.count())