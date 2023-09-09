from cgi import print_environ
import collections
from pydoc import cli
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv(override=False)

uri = os.getenv('DATABASE_URL')

client = MongoClient(uri, server_api=ServerApi('1'))
    
Database = client.get_database('proyect-tutorIA')
CTGrammar = Database.get_collection('Grammar')
CTText = Database.get_collection('Text')
CTUser = Database.get_collection('User')
CTVocabulary = Database.get_collection('Vocabulary')