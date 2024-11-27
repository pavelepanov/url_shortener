from abc import ABC, abstractmethod
from uuid import UUID


class UUIDGenerator(ABC):
    @abstractmethod
    def __call__(self) -> UUID:
        ...
