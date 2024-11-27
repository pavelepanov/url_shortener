from url_shortener.application.contracts.url.requests import GetFullUrlByShortUrlRequest
from url_shortener.application.contracts.url.responses import ShortUrlResponse
from url_shortener.entrypoint.ioc import IoC


async def get_full_url_by_short_url(
    ioc: IoC, request: GetFullUrlByShortUrlRequest
) -> ShortUrlResponse:
    with ioc.get_full_url_by_short_url() as get_full_url_by_short_url_interactor:
        return await get_full_url_by_short_url_interactor(request)
