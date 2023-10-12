from pymongo import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv(override=False)

uri = os.getenv('Database_URL')

client = MongoClient(uri, server_api=ServerApi('1'))

DatabaseName = client.get_database('proyect-tutorIA')
CTGrammar = DatabaseName.get_collection('Grammar')
CTText = DatabaseName.get_collection('Text')
CTUser = DatabaseName.get_collection('User')
CTVocabulary = DatabaseName.get_collection('Vocabulary')