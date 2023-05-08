import pytest

from src.rest_api import Api
from config import Parameters


@pytest.fixture()
def api():
    return Api(url=Parameters.url, token=Parameters.token, key=Parameters.key)
