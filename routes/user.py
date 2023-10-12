import imp
from unittest import result
from bson import ObjectId
from fastapi import APIRouter, status,Response, HTTPException
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from models.models import UserModel

from fastapi import APIRouter
from config.database import  CTafrica, CTamerica, CTasia, CTeuropa, CToceania, CTuser
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/users', tags=["users"])
async def find_all_users():
    return usersEntity(CTuser.find())

@user.post('/user', tags=["users"],  description="create user")
async def create_user(user : UserModel):
    new_user = dict(user)
    CTuser.insert_one(new_user).inserted_id
    created_user = CTuser.find({"email": new_user["email"]})

    return usersEntity(created_user)

@user.get('/user/{email},{password}', tags=["users"],  description="login for users")
async def login_user(email : str, passw : str):
    
    user = CTuser.find_one({"email": str(email),
                            "password": str(passw)})
    
    if not user:
         return HTTPException(status_code=404, detail="contrañsena o usuario incorrecto")
    else:
        return(userEntity(user))
    
"""
@user.get('/user/{id}')
def find_user():
    return "hello wordl"

@user.put('/user/{id}')
def update_user():
    return "hello wordl"

@user.delete('/user/{id}')
def delete_user():
    return "hello wordl" """