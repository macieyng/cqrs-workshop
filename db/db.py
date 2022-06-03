import abc
from dataclasses import dataclass
import json

from app.types import Document


class IDB(abc.ABC):
    _collection: dict[Document]

    @abc.abstractmethod
    def get(self, _id: str):
        pass
    
    @abc.abstractmethod
    def find(self, **kwargs):
        pass
    
    @abc.abstractmethod
    def save(self, obj: Document):
        pass
    
    
class IRepo(abc.ABC):
    @abc.abstractmethod
    def load(self) -> dict:
        pass
    
    @abc.abstractmethod
    def persist(self, obj: Document) -> None:
        pass
    

class InMemoryRepo(IRepo):
    def __init__(self) -> None:
        self.data = {}
    
    def load(self) -> dict:
        return self.data
    
    def persist(self, obj: Document) -> None:
        self.data.update(obj)


class JSONPersistance(IRepo):
    def __init__(self, name: str) -> None:
        self.name: str = name 
        
    def load(self) -> dict:
        with open(f"{self.name}.json", "r") as f:
            data = f.read()
        return json.loads(data)
    
    def persist(self, obj: Document):
        with open(f"{self.name}.json", "r") as f:
            data = f.read()

        collection: dict = json.loads(data)
        collection.update(obj)
        data = json.dumps(collection)
        
        with open(f"{self.name}.json", "w") as f:
            f.write(data)

    
class DB(IDB):
    def __init__(self, peristance: JSONPersistance) -> None:
        self.persistance = peristance
        self._collection = self.persistance.load()
    
    def get(self, _id: str):
        name = self._collection[_id]
        return {_id: name}
    
    def find(self, name: str):
        list_of_obj = list(self._collection.items())
        
        return [{key: value} for key, value in filter(lambda x: x[1] == name, list_of_obj)]

    def save(self, obj: Document):
        self.persistance.persist(obj)
        self._collection = self.persistance.load()


class UserDB(DB):
    def __init__(self, peristance: IRepo = JSONPersistance("users")) -> None:
        super().__init__(peristance)
