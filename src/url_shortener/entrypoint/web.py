import asyncio
import uuid
from url_shortener.infrastructure.config import DomainUrl
from url_shortener.entrypoint.ioc import IoC

from url_shortener.presentation.web_api.create_short_url import create_short_url

from url_shortener.application.contracts.url.requests import CreateShortUrlRequest

from url_shortener.infrastructure.adapters.short_url_id_generator_uuid import UUIDShortUrlGenerator


DictionaryDatabase = dict()

request = CreateShortUrlRequest(
    full_url='http://google.com',
)
request2 = CreateShortUrlRequest(
    full_url='http://gfg.com',
)


ioc = IoC(domain_url=DomainUrl.from_env(), database=DictionaryDatabase, id_generator_short_url=UUIDShortUrlGenerator())


if __name__ == '__main__':
    print(asyncio.run(create_short_url(ioc=ioc, request=request)))
    print(asyncio.run(create_short_url(ioc=ioc, request=request2)))
    print(asyncio.run(create_short_url(ioc=ioc, request=request)))

