from cgi import print_environ
import collections
from pydoc import cli
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv(override=False)

DBuser = os.getenv('DBUSER')
DBpass = os.getenv('DBPASS')
DBname = os.getenv('DBNAME')
DBcluster = os.getenv('DBCLUSTER')
collectionsDB = [os.getenv('CTGRAMAR'), os.getenv('CTVOCABULARY'), os.getenv('CTTEXT'), os.getenv('CTUSER'),]

print(DBuser)
print(DBpass)
print(DBcluster)

uri = f"mongodb+srv://{DBuser}:{DBpass}@{DBcluster}.nsqsaun.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

Database = client.get_database(DBname)

CTgramar = Database.get_collection(collectionsDB[0])
CTvocabulary = Database.get_collection(collectionsDB[2])
CTtext = Database.get_collection(collectionsDB[2])
CTuser = Database.get_collection(collectionsDB[3])

data = CTtext.find()

for doc in data:
  print(doc)
  