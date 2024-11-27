from url_shortener.domain.repositories.short_url import ShortUrlRepository
from url_shortener.domain.value_objects.full_url import FullUrl
from url_shortener.domain.entities.short_url import ShortUrl, short_url_factory
from url_shortener.application.protocols.id_generator import UUIDGenerator
from url_shortener.infrastructure.errors.error import AlreadyExists


class DictionaryShortUrlRepository(ShortUrlRepository):
    def __init__(self, database: dict, id_generator: UUIDGenerator) -> None:
        self.database = database
        self.id_generator = id_generator

    async def create(self, full_url: FullUrl, short_url: str) -> ShortUrl:
        if full_url not in self.database:
            short_url_entity = short_url_factory(
                id=self.id_generator(),
                full_url=full_url.full_url,
                short_url=short_url
            )

            self.database[short_url_entity.id] = short_url

            return short_url_entity

        else:
            raise AlreadyExists('This url already exists in database')
