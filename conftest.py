import pytest
from api_client.auth_api import AuthApi
from api_client.users_api import UsersApi
from faker import Faker

@pytest.fixture()
def fake():
    return Faker()

@pytest.fixture()
def users_endpoint():
    return UsersApi()

@pytest.fixture()
def auth_endpoint():
    return AuthApi()
