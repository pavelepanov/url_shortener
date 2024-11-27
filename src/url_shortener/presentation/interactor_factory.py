from abc import ABC, abstractmethod
from typing import ContextManager

from url_shortener.application.usecases.create_short_url import CreateShortUrl


class InteractorFactory(ABC):
    @abstractmethod
    def create_short_url(self) -> ContextManager[CreateShortUrl]:
        raise NotImplementedError
