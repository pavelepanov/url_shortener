from url_shortener.application.protocols.interactor import Interactor
from url_shortener.application.contracts.url.requests import GetFullUrlByShortUrlRequest
from url_shortener.application.contracts.url.responses import ShortUrlResponse
from url_shortener.domain.repositories.short_url import ShortUrlRepository
from url_shortener.domain.value_objects.short_url import ShortUrl


class GetByFullUrl(Interactor[GetFullUrlByShortUrlRequest, ShortUrlResponse]):
    def __init__(self, short_url_repository: ShortUrlRepository):
        self.short_url_repository = short_url_repository

    async def __call__(self, request: GetFullUrlByShortUrlRequest) -> ShortUrlResponse:
        short_url = await self.short_url_repository.get_by_short_url(short_url=ShortUrl(request.short_url))

        return ShortUrlResponse(
            id=short_url.id.id,
            full_url=short_url.full_url.full_url,
            short_url=short_url.short_url.short_url,
        )
