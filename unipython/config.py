''' configuration module
'''

from functools import lru_cache
from pydantic import BaseSettings
import secrets


class Configuration(BaseSettings):
        env_name: str = "Local"
        token: str = ""
        base_url : str = "http://127.0.0.1:8080"
        host_url : str = ""
        secret_key: str = secrets.token_hex(16)

        class Config:
                env_file = ".env"


@lru_cache
def get_configuration() -> Configuration:
        configuraton = Configuration()
        print(f"Loading configuration from {configuraton.env_name}")
        return configuraton
