from abc import ABC, abstractmethod


class ValueObject(ABC):
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    @abstractmethod
    def _validate(self) -> None:
        ...
