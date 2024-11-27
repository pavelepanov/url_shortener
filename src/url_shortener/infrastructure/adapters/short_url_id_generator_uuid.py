from uuid import UUID, uuid4

from url_shortener.application.protocols.id_generator import UUIDGenerator


class UUIDShortUrlGenerator(UUIDGenerator):
    def __call__(self) -> UUID:
        return uuid4()
