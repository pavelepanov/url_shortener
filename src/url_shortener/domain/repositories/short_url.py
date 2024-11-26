from typing import Protocol

from url_shortener.domain.entities.short_url import ShortUrl
from url_shortener.domain.value_objects.full_url import FullUrl


class ShortUrlRepository(Protocol):
    async def get_by_short_url(self, full_url: FullUrl) -> ShortUrl:
        raise NotImplementedError

    async def create(self, full_url: FullUrl) -> ShortUrl:
        raise NotImplementedError
