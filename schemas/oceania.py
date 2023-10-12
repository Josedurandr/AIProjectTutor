def oceaniaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty_level"],
    }
    
def oceaniasEntity(entity) -> list:
    return [oceaniaEntity(item) for item in entity]