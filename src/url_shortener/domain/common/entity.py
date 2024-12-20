from typing import TypeVar

EntityId = TypeVar("EntityId")


class Entity:
    def __init__(self, id: EntityId):
        self.id = id

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
