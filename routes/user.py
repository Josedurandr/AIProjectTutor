from bson import ObjectId
from fastapi import APIRouter, status,Response
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from fastapi import APIRouter
from config.database import client, CTText, CTGrammar, CTUser, CTVocabulary
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/users', tags=["users"])
async def find_all_users():
    return usersEntity(CTUser.find())

@user.get('/user')
def create_user():
    return "hello wordl"

@user.get('/user/{id}')
def find_user():
    return "hello wordl"

@user.put('/user/{id}')
def update_user():
    return "hello wordl"

@user.delete('/user/{id}')
def delete_user():
    return "hello wordl"