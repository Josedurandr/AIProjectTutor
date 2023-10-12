import config.database as database

def test_connection_database():
  try:
     database.client.admin.command('ping')
     print("Pinged your deployment. You successfully connected to MongoDB!")
  except Exception as e:
     print(e)
     exit(1)