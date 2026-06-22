import urllib3

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from data import (
    BASE_URL,
    CREATE_ADVERTISEMENT_ENDPOINT,
    DELETE_ADVERTISEMENT_ENDPOINT,
    LOGIN_ENDPOINT,
    REGISTER_ENDPOINT,
    TIMEOUT,
    UPDATE_ADVERTISEMENT_ENDPOINT,
    VERIFY_SSL,
)
from utils import get_test_image_file

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
            "Accept": "application/json, text/plain, */*",
        }

    @staticmethod
    def _build_listing_encoder(payload, include_existing_image=False):
        fields = {
            "name": str(payload["name"]),
            "category": str(payload["category"]),
            "condition": str(payload["condition"]),
            "city": str(payload["city"]),
            "description": str(payload["description"]),
            "price": str(payload["price"]),
        }

        if include_existing_image:
            fields["img1"] = str(payload["img1"])
            fields["img2"] = str(payload["img2"])

        fields["images"] = get_test_image_file()

        return MultipartEncoder(fields=fields)

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
        encoder = self._build_listing_encoder(payload)

        headers = self._get_auth_headers(token)
        headers["Content-Type"] = encoder.content_type

        return self.session.post(
            self._make_url(CREATE_ADVERTISEMENT_ENDPOINT),
            data=encoder,
            headers=headers,
            timeout=TIMEOUT,
            verify=VERIFY_SSL,
        )

    def update_advertisement(self, token, advertisement_id, payload):
        encoder = self._build_listing_encoder(payload, include_existing_image=True)

        headers = self._get_auth_headers(token)
        headers["Content-Type"] = encoder.content_type

        return self.session.patch(
            self._make_url(f"{UPDATE_ADVERTISEMENT_ENDPOINT}/{advertisement_id}"),
            data=encoder,
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