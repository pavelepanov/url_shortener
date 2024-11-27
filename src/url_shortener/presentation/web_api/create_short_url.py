from url_shortener.application.contracts.url.requests import CreateShortUrlRequest
from url_shortener.domain.entities.short_url import ShortUrl
from url_shortener.entrypoint.ioc import IoC


async def create_short_url(ioc: IoC, request: CreateShortUrlRequest) -> ShortUrl:
    with ioc.create_short_url() as create_short_url_interactor:
        return await create_short_url_interactor(request)
