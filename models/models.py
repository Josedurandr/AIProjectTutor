from unicodedata import category, name
from mongoengine import Document, fields
from bson import ObjectId 
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    email: str
    password: str
    skill_level: dict
    experience_level: dict


class AfricaModel(BaseModel):
    country: str
    capital: str
    difficulty_level: int
    
class AmericaModel(BaseModel):
    country: str
    capital: str
    difficulty_level: int
    
class AsiaModel(BaseModel):
    country: str
    capital: str
    difficulty_level: int

class EuropaModel(BaseModel):
    country: str
    capital: str
    difficulty_level: int

class OceaniaModel(BaseModel):
    country: str
    capital: str
    difficulty_level: int