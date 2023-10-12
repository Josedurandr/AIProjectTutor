from fastapi import APIRouter, status,Response, HTTPException
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from fastapi import APIRouter
from config.database import  CTafrica, CTamerica, CTasia, CTeuropa, CToceania, CTuser
from schemas.europa import europasEntity

europa = APIRouter()

@europa.get('/europa', tags=["continets"])
async def find_all_countries():
    return europasEntity(CTeuropa.find())

@europa.get('/europaRandom/{email}', tags=["continents_level"])
async def find_countries_by_level(email: str):

    user = CTuser.find_one({"email": str(email)})

    if not user:
        return HTTPException(status_code=404, detail="Usuario no encontrado")
    
    else:    
      user_skill_level_europa = user.get("skill_level", {}).get("europa", 0)

      countries = CTeuropa.find({"difficulty": {"$lte": user_skill_level_europa}})
      
      return europasEntity(countries)