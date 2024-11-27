from dataclasses import dataclass


@dataclass(frozen=True)
class ShortUrlResponse:
    id: int
    full_url: str
    short_url: str


@dataclass(frozen=True)
class FullUrlResponse:
    full_url: str
