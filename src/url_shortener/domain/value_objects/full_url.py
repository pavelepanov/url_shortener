import logging
from re import match

from url_shortener.domain.common.errors import ValueObjectValidationError
from url_shortener.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class FullUrl(ValueObject):
    def __init__(self, full_url: str):
        self.__full_url = full_url
        self._validate()

    def _validate(self) -> None:
        try:
            url_pattern = r'(https?://[\S]+)'

            if not isinstance(self.__full_url, str):
                raise ValueObjectValidationError(
                    f'Full url must be a str, not {type(self.__full_url)}'
                )

            if len(self.__full_url) > 2083:
                raise ValueObjectValidationError(
                    f'Length of full url must be less then 2083 symbols, now length is f{len(self.__full_url)}'
                )

            if len(self.__full_url) <= 0:
                raise ValueObjectValidationError(
                    f'Length of full url must be more then 0 symbols, now length is f{len(self.__full_url)}'
                )

            if not match(url_pattern, self.__full_url):
                raise ValueObjectValidationError(
                    'Invalid full url format. Url full must be in the format http://localhost:8000'
                )
        except Exception as e:
            logging.exception('Full url did not create because %s' % e)

    @property
    def full_url(self):
        return self.__full_url
