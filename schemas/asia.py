def asiaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty_level"],
    }
    
def asiasEntity(entity) -> list:
    return [asiaEntity(item) for item in entity]