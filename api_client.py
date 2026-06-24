import urllib3

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from config import (
    BASE_URL,
    CREATE_ADVERTISEMENT_ENDPOINT,
    DELETE_ADVERTISEMENT_ENDPOINT,
    LOGIN_ENDPOINT,
    REGISTER_ENDPOINT,
    TIMEOUT,
    UPDATE_ADVERTISEMENT_ENDPOINT,
    VERIFY_SSL,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
        })

    def _make_url(self, endpoint):
        return f"{BASE_URL}{endpoint}"

    @staticmethod
    def _get_auth_headers(token):
        return {
            "Authorization": f"Bearer {token}",
        }

    @staticmethod
    def _prepare_multipart_fields(payload):
        return {
            key: value if isinstance(value, str) else str(value)
            for key, value in payload.items()
        }

    def register_user(self, payload):
        return self.session.post(
            self._make_url(REGISTER_ENDPOINT),
            json=payload,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

    def login_user(self, payload):
        return self.session.post(
            self._make_url(LOGIN_ENDPOINT),
            json=payload,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

    def create_advertisement(self, token, payload):
        multipart_data = MultipartEncoder(
            fields=self._prepare_multipart_fields(payload)
        )
        headers = self._get_auth_headers(token)
        headers["Content-Type"] = multipart_data.content_type

        return self.session.post(
            self._make_url(CREATE_ADVERTISEMENT_ENDPOINT),
            data=multipart_data,
            headers=headers,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

    def update_advertisement(self, token, advertisement_id, payload):
        multipart_data = MultipartEncoder(
            fields=self._prepare_multipart_fields(payload)
        )
        headers = self._get_auth_headers(token)
        headers["Content-Type"] = multipart_data.content_type

        return self.session.patch(
            self._make_url(f"{UPDATE_ADVERTISEMENT_ENDPOINT}/{advertisement_id}"),
            data=multipart_data,
            headers=headers,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

    def delete_advertisement(self, token, advertisement_id):
        return self.session.delete(
            self._make_url(f"{DELETE_ADVERTISEMENT_ENDPOINT}/{advertisement_id}"),
            headers=self._get_auth_headers(token),
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )