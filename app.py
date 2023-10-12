from routes.user import user
from dotenv import load_dotenv
from fastapi import FastAPI, Body, HTTPException, status

load_dotenv()

app = FastAPI()

app.include_router(user)