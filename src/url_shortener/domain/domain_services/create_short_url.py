import hashlib


def create_short_url(base_url: str, full_url: str) -> str:
    short_hash = hashlib.md5(full_url.encode()).hexdigest()[:6]

    short_url = 'http://' + base_url + short_hash

    return short_url
