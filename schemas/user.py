def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "preferred_languages": item["preferred_languages"],
        "skill_level": item["skill_level"],
        "experience_level": item["experience_level"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
