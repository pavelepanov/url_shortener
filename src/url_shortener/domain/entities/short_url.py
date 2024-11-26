from url_shortener.domain.common.entity import Entity
from url_shortener.domain.value_objects.short_url_id import ShortUrlId
from url_shortener.domain.value_objects.full_url import FullUrl


class ShortUrl(Entity):
    def __init__(self, id: ShortUrlId, full_url: FullUrl) -> None:
        super().__init__(id=id)
        self.full_url = full_url


def short_url_factory(
        id: int,
        full_url: str,
) -> ShortUrl:
    return ShortUrl(
        id=ShortUrlId(id),
        full_url=FullUrl(full_url),
    )

