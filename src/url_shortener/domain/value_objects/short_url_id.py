import logging
from uuid import UUID

from url_shortener.domain.common.errors import ValueObjectValidationError
from url_shortener.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class ShortUrlId(ValueObject):
    def __init__(self, id: UUID):
        self.__id = id
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__id, UUID):
                raise ValueObjectValidationError(
                    f'Short url id must be an UUID, not {type(self.__id)}'
                )
        except Exception as e:
            logging.exception('Short url id did not create because %s' % e)

    @property
    def id(self):
        return self.__id
