from api_client.base_api import BaseApi


class AuthApi(BaseApi):

    def login_user_post(self, payload: dict):
        self.method_post(
            endpoint="/login",
            payload=payload
        )
        return self.response_json

    def register_user_post(self, payload: dict):
        self.method_post(
            endpoint="/register",
            payload=payload
        )
        return self.response_json
