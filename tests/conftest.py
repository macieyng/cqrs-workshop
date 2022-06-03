import pytest
from db.db import UserDB, InMemoryRepo


@pytest.fixture(autouse=True)
def user_db():
    print("setup")
    yield UserDB(InMemoryRepo())
    print("teardown")
