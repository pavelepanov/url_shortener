from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class DomainUrl:
    domain_url: str

    @staticmethod
    def from_env() -> 'DomainUrl':
        domain_url = getenv('DOMAIN_URL')

        return DomainUrl(str(domain_url))


