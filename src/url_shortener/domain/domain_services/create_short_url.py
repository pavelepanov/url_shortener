import hashlib
import logging

logger = logging.getLogger(__name__)


def create_short_url(base_url: str, full_url: str) -> str:
    try:
        short_hash = hashlib.md5(full_url.encode()).hexdigest()[:6]

        short_url = 'http://' + base_url + short_hash

        logging.info('Short url was created')

        return short_url
    except Exception as e:
        logging.exception('Short url did not create because %s' % e)
