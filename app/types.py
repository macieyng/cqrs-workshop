from typing import TypeAlias
from uuid import UUID


UserId: TypeAlias = UUID
UserName: TypeAlias = str
Document: TypeAlias = dict[UUID, str]
User: TypeAlias = dict[UserId, UserName]
