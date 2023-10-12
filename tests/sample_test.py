import os
from dotenv import load_dotenv
from pymongo import MongoClient 
from pymongo.server_api import ServerApi

load_dotenv(override=False)

uri = os.getenv('Database_URL')

client = MongoClient(uri, server_api=ServerApi('1'))

def test_connection_database():
  try:
     client.admin.command("ping")
     print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
     print(e)
     exit(1)

test_connection_database()
