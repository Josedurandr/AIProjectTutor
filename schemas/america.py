def americaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty"],
    }
    
def americasEntity(entity) -> list:
    return [americaEntity(item) for item in entity]