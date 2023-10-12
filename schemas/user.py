def userEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        "skill_level": str(item["skill_level"]),
        "experience_level": str(item["experience_level"])
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
 