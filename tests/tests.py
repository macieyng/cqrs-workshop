from typing import TYPE_CHECKING
from app.code import get_user_by_id, search_by_name, upsert_user
from app.types import User, UserId
from uuid import uuid4

if TYPE_CHECKING:
    from db.db import UserDB


def test_get_user_by_id(user_db: "UserDB"):
    _id: UserId = uuid4().hex
    user: User = {_id: "username"}
    upsert_user(user, user_db)
    
    fetched_user = get_user_by_id(_id, user_db)
    
    assert fetched_user == user
    
def test_search_by_name(user_db: "UserDB"):
    _id: UserId = uuid4().hex
    user: User = {_id: "username"}
    upsert_user(user, user_db)
    
    _id: UserId = uuid4().hex
    user: User = {_id: "socek"}
    upsert_user(user, user_db)
    
    fetched_users = search_by_name("socek", user_db)
    
    assert user in fetched_users


def test_upsert_user(user_db: "UserDB"):
    _id: UserId = uuid4().hex
    user: User = {_id: "username"}
    
    upsert_user(user, user_db)
    
    user = get_user_by_id(_id, user_db)
    
    assert user is not None