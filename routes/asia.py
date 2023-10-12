from fastapi import APIRouter, status,Response, HTTPException
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from fastapi import APIRouter
from config.database import  CTafrica, CTamerica, CTasia, CTeuropa, CToceania, CTuser
from schemas.asia import asiasEntity

asia = APIRouter()

@asia.get('/asia', tags=["continets"])
async def find_all_countries():
    return asiasEntity(CTasia.find())

@asia.get('/asiaRandom/{email}', tags=["continents_level"])
async def find_countries_by_level(email: str):

    user = CTuser.find_one({"email": str(email)})

    if not user:
        return HTTPException(status_code=404, detail="Usuario no encontrado")
    
    else:    
      user_skill_level_asia = user.get("skill_level", {}).get("asia", 0)

      countries = CTasia.find({"difficulty_level": {"$lte": user_skill_level_asia}})
      
      return asiasEntity(countries)