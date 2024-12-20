from uuid import UUID

from url_shortener.domain.common.entity import Entity
from url_shortener.domain.value_objects.full_url import FullUrl
from url_shortener.domain.value_objects.short_url_id import ShortUrlId


class ShortUrl(Entity):
    def __init__(self, id: ShortUrlId, full_url: FullUrl, short_url: str) -> None:
        super().__init__(id=id)
        self.full_url = full_url
        self.short_url = short_url


def short_url_factory(
    id: UUID,
    full_url: str,
    short_url: str,
) -> ShortUrl:
    return ShortUrl(
        id=ShortUrlId(id),
        full_url=FullUrl(full_url),
        short_url=short_url,
    )
