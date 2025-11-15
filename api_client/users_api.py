from api_client.base_api import BaseApi


class UsersApi(BaseApi):


    def create_user_post(self, payload: dict):
        self.method_post(
            endpoint="/users",
            payload=payload
        )
        return self.response_json

    def recive_all_users_get(self):
        self.method_get(
            endpoint="/users"
        )
        return self.response_json

    def recieve_user_by_id_get(self, user_id: int):
        self.method_get(
            endpoint=f"/users/{user_id}"
        )
        return self.response_json

    def update_user_put(self, user_id: int, payload: dict):
        self.method_put(
            endpoint=f"/users/{user_id}",
            payload=payload
        )
        return self.response_json

    def update_user_patch(self, user_id: int, payload: dict):
        self.method_patch(
            endpoint=f"/users/{user_id}",
            payload=payload
        )
        return self.response_json

    def delete_user_delete(self, user_id: int):
        self.method_delete(
            endpoint=f"/users/{user_id}"
        )
        return self.response
