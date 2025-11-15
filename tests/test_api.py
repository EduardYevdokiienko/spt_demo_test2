import pytest


def test_login_user_valid(auth_endpoint):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    auth_endpoint.login_user_post(payload)
    auth_endpoint.assert_status_code_is(200)
    auth_endpoint.assert_response_token_is_not_none()

@pytest.mark.parametrize("payload, expected_error", [
    ({"email": "peter@klaven"}, "Missing password"),
    ({}, "Missing email or username"),
])
def test_login_user_missing_fields(auth_endpoint, payload, expected_error):
    auth_endpoint.login_user_post(payload)
    auth_endpoint.assert_status_code_is(400)
    auth_endpoint.assert_response_field("error", expected_error)

def test_login_user_invalid_credentials(auth_endpoint, fake):
    payload = {
        "email": fake.email(),
        "password": fake.password()
    }
    auth_endpoint.login_user_post(payload)
    auth_endpoint.assert_status_code_is(400)
    assert "error" in auth_endpoint.response_json

@pytest.mark.parametrize("payload", [
    {"name": "Alice", "age": "25", "city": "NY"},
    {"name": "", "age": "25", "city": "NY"},
    {"name": "Bob", "age": "-5", "city": "LA"},
    {"name": "Charlie", "age": "thirty", "city": "SF"},
    {"name": "Diana", "age": "28"},
])
def test_create_user(users_endpoint, payload):
    users_endpoint.create_user_post(payload)
    users_endpoint.assert_status_code_is(201)
    users_endpoint.assert_response_id_is_not_none()
    users_endpoint.assert_response_contains_payload(payload)
    assert "createdAt" in users_endpoint.response_json

def test_recive_all_users(users_endpoint):
    users_endpoint.recive_all_users_get()
    users_endpoint.assert_status_code_is(200)

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_recieve_user_by_id_positive(users_endpoint, user_id):
    users_endpoint.recieve_user_by_id_get(user_id)
    users_endpoint.assert_status_code_is(200)
    users_endpoint.assert_response_field("data.id", user_id)
    email = users_endpoint.response_json["data"]["email"]
    assert "@" in email

@pytest.mark.parametrize("user_id", [23, 999, -1])
def test_recieve_user_by_id_not_found(users_endpoint, user_id):
    users_endpoint.recieve_user_by_id_get(user_id)
    users_endpoint.assert_status_code_is(404)

def test_update_user_put(users_endpoint, fake):
    payload = {
        "name": fake.first_name(),
        "age": str(fake.random_int(18, 80)),
        "city": fake.city()
    }
    users_endpoint.update_user_put(1, payload)
    users_endpoint.assert_status_code_is(200)
    users_endpoint.assert_response_contains_payload(payload)
    assert "updatedAt" in users_endpoint.response_json

def test_update_user_patch(users_endpoint, fake):
    payload = {
        "name": fake.first_name(),
    }
    users_endpoint.update_user_patch(1, payload)
    users_endpoint.assert_status_code_is(200)
    users_endpoint.assert_response_contains_payload(payload)
    assert "updatedAt" in users_endpoint.response_json

def test_delete_user(users_endpoint):
    users_endpoint.delete_user_delete(1)
    users_endpoint.assert_status_code_is(204)
    assert users_endpoint.response_json == {}
