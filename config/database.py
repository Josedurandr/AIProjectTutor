from pymongo import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv(override=False)

uri = os.getenv('Database_URL')

client = MongoClient(uri, server_api=ServerApi('1'))

databaseName = client.get_database('TriviaWorld')

CTafrica = databaseName.get_collection('Africa')
CTamerica = databaseName.get_collection('America')
CTasia = databaseName.get_collection('Asia')
CTeuropa = databaseName.get_collection('Europa')
CToceania = databaseName.get_collection('Oceania')
CTuser = databaseName.get_collection('User')

