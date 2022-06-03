from db.db import UserDB
from app.types import UserId, UserName



def get_user_by_id(user_id: UserId, user_db: UserDB = UserDB()) -> dict[UserId, UserName]:
    return user_db.get(user_id)


def search_by_name(user_name: UserName, user_db: UserDB = UserDB()) -> list[dict[UserId, UserName]]:
    return user_db.find(name=user_name)


def upsert_user(user: dict[UserId, UserName], user_db: UserDB = UserDB()):
    user_db.save(user)
