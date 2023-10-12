def oceaniaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty"],
    }
    
def oceaniasEntity(entity) -> list:
    return [oceaniaEntity(item) for item in entity]