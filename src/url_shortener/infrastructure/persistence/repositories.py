from url_shortener.application.protocols.id_generator import UUIDGenerator
from url_shortener.domain.entities.short_url import ShortUrl, short_url_factory
from url_shortener.domain.repositories.short_url import ShortUrlRepository
from url_shortener.domain.value_objects.full_url import FullUrl
from url_shortener.infrastructure.errors.error import AlreadyExists, DoesNotExists


class DictionaryShortUrlRepository(ShortUrlRepository):
    def __init__(self, database: dict, id_generator: UUIDGenerator) -> None:
        self.database = database
        self.id_generator = id_generator

    async def create(self, full_url: FullUrl, short_url: str) -> ShortUrl:
        is_full_url_in_database = False
        for full_short_urls in self.database.values():
            if full_url.full_url in full_short_urls:
                is_full_url_in_database = True
                break

        if not is_full_url_in_database:
            short_url_entity = short_url_factory(
                id=self.id_generator(), full_url=full_url.full_url, short_url=short_url
            )

            self.database[short_url_entity.id.id] = (
                short_url_entity.full_url.full_url,
                short_url_entity.short_url,
            )

            return short_url_entity

        else:
            raise AlreadyExists("This url already exists in database")

    async def get_by_short_url(self, short_url: ShortUrl) -> FullUrl:
        is_short_url_in_database = False
        for full_short_urls in self.database.values():
            if short_url.short_url in full_short_urls:
                is_short_url_in_database = True
                break

        if is_short_url_in_database:
            for key, value in self.database.items():
                if value[1] == short_url.short_url:
                    return value[0]
        else:
            raise DoesNotExists("This short url does not exists in database")
