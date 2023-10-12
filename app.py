from routes.user import user
from routes.africa import africa
from routes.america import america
from routes.asia import asia
from routes.europa import europa
from routes.oceania import oceania

from dotenv import load_dotenv
from fastapi import FastAPI, Body, HTTPException, status

load_dotenv()

app = FastAPI()

app.include_router(user)
app.include_router(africa)
app.include_router(america)
app.include_router(asia)
app.include_router(europa)

