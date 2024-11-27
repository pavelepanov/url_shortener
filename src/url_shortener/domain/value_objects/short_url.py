
from url_shortener.domain.common.errors import ValueObjectValidationError
from url_shortener.domain.common.value_object import ValueObject


class ShortUrl(ValueObject):
    def __init__(self, short_url: str):
        self.__short_url = short_url
        self._validate()

    def _validate(self) -> None:
        if not isinstance(self.__short_url, str):
            raise ValueObjectValidationError(
                f"Full url must be a str, not {type(self.__short_url)}"
            )

    @property
    def short_url(self):
        return self.__short_url
