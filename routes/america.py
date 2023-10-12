from fastapi import APIRouter, status,Response, HTTPException
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from fastapi import APIRouter
from config.database import  CTafrica, CTamerica, CTasia, CTeuropa, CToceania, CTuser
from schemas.america import americasEntity

america = APIRouter()

@america.get('/america', tags=["continets"])
async def find_all_countries():
    return americasEntity(CTamerica.find())

@america.get('/americaRandom/{email}', tags=["continents_level"])
async def find_countries_by_level(email: str):

    user = CTuser.find_one({"email": str(email)})

    if not user:
        return HTTPException(status_code=404, detail="Usuario no encontrado")
    
    else:    
      user_skill_level_america = user.get("skill_level", {}).get("america", 0)

      countries = CTamerica.find({"difficulty": {"$lte": user_skill_level_america}})
      
      return americasEntity(countries)