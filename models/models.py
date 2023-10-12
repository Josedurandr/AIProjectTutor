from unicodedata import category, name
from mongoengine import Document, fields
from bson import ObjectId 
from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class GrammarModel(BaseModel):
    rule: str
    explanation: str
    examples: List[str]

class VocabularyModel(BaseModel):
    word: str
    translation: str

class TextModel(BaseModel):
    text: str
    language: str
    category: int

class UserModel(BaseModel):
    email: str
    preferred_languages: List[str]
    skill_level: dict
    experience_level: dict
