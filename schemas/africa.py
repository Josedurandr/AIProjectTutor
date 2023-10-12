def africaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty_level"],
    }
    
def africasEntity(entity) -> list:
    return [africaEntity(item) for item in entity]