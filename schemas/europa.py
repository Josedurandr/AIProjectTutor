def europaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "country": item["country"],
        "difficulty": item["difficulty"],
    }
    
def europasEntity(entity) -> list:
    return [europaEntity(item) for item in entity]