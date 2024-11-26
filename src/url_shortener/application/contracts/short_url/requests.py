from dataclasses import dataclass


@dataclass(frozen=True)
class GetFullUrlByShortUrl:
    short_url: str


@dataclass(frozen=True)
class CreateShortUrl:
    full_url: str
