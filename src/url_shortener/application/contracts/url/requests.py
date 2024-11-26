from dataclasses import dataclass


@dataclass(frozen=True)
class GetFullUrlByShortUrlRequest:
    short_url: str


@dataclass(frozen=True)
class CreateShortUrlRequest:
    full_url: str
