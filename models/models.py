from unicodedata import category, name
from mongoengine import Document, fields
from bson import ObjectId 
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str
    email: str
    password: str
    skill_level: dict = Field(default={"africa": 1, "america": 1, "asia": 1, "europa": 1, "oceania": 1})
    experience_level: dict = Field(default={"africa": 0, "america": 0, "asia": 0, "europa": 0, "oceania": 0})


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