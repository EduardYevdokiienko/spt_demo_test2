import requests

from constant import BASE_URL, HEADERS


class BaseApi:
    response: requests.Response
    response_json: dict


    def _request(self, method: str, endpoint: str, payload=None, headers= HEADERS):
        url = f"{BASE_URL}{endpoint}"
        self.response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=payload
        )
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = {}
        return self.response


    def method_post(self, endpoint: str, payload: dict):
        return self._request("POST", endpoint, payload=payload)

    def method_get(self, endpoint: str):
        return self._request("GET", endpoint)

    def method_put(self, endpoint: str, payload: dict):
        return self._request("PUT", endpoint, payload=payload)

    def method_patch(self, endpoint: str, payload: dict):
        return self._request("PATCH", endpoint, payload=payload)

    def method_delete(self, endpoint: str):
        return self._request("DELETE", endpoint)


    def assert_status_code_is(self, status_code):
        assert self.response.status_code == status_code

    def assert_response_field(self, field, expected_value):
        value = self.response_json
        for key in field.split("."):
            value = value[key]
        assert value == expected_value

    def assert_response_id_is_not_none(self):
        assert self.response_json.get('id') is not None

    def assert_response_token_is_not_none(self):
        assert self.response_json.get('token') is not None

    def assert_response_contains_payload(self, payload: dict):
        for key, value in payload.items():
            assert self.response_json.get(key) == value
