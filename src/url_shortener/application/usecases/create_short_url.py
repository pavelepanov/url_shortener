from url_shortener.application.protocols.interactor import Interactor
from url_shortener.application.contracts.url.requests import CreateShortUrlRequest
from url_shortener.application.contracts.url.responses import ShortUrlResponse
from url_shortener.domain.repositories.short_url import ShortUrlRepository
from url_shortener.domain.value_objects.full_url import FullUrl


class CreateShortUrl(Interactor[CreateShortUrlRequest, ShortUrlResponse]):
    def __init__(self, short_url_repository: ShortUrlRepository):
        self.short_url_repository = short_url_repository

    async def __call__(self, request: CreateShortUrlRequest) -> ShortUrlResponse:
        short_url = await self.short_url_repository.create(
            full_url=FullUrl(request.full_url),
        )

        return ShortUrlResponse(
            id=short_url.id.id,
            full_url=short_url.full_url.full_url,
            short_url=short_url.short_url.short_url,
        )
