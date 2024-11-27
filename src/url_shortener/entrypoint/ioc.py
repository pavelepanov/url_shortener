from contextlib import contextmanager

from url_shortener.application.usecases.create_short_url import CreateShortUrl
from url_shortener.application.usecases.get_by_short_url import GetByShortUrl
from url_shortener.infrastructure.adapters.short_url_id_generator_uuid import \
    UUIDShortUrlGenerator
from url_shortener.infrastructure.config import DomainUrl
from url_shortener.infrastructure.persistence.repositories import \
    DictionaryShortUrlRepository
from url_shortener.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    def __init__(
        self,
        domain_url: DomainUrl,
        database: dict,
        id_generator_short_url: UUIDShortUrlGenerator,
    ):
        self.short_url_repository = DictionaryShortUrlRepository(
            database=database, id_generator=id_generator_short_url
        )
        self.domain_url = domain_url.from_env().domain_url

    @contextmanager
    def create_short_url(self) -> CreateShortUrl:
        yield CreateShortUrl(
            short_url_repository=self.short_url_repository,
            base_url=self.domain_url,
        )

    @contextmanager
    def get_full_url_by_short_url(self) -> GetByShortUrl:
        yield GetByShortUrl(
            short_url_repository=self.short_url_repository,
        )
