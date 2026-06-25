from data import EXPECTED_STATUS_CODES
from helpers import build_update_advertisement_payload
from utils import extract_title, get_response_json


class TestUpdateAdvertisement:
    def test_successful_update_advertisement_field(self, api_client, created_advertisement):
        payload = build_update_advertisement_payload(created_advertisement["image_url"])

        response = api_client.update_advertisement(
            created_advertisement["owner"]["token"],
            created_advertisement["id"],
            payload,
        )
        response_json = get_response_json(response)

        assert response.status_code == EXPECTED_STATUS_CODES["update_advertisement_success"]
        assert extract_title(response_json) == payload["name"]

    def test_user_cannot_update_foreign_advertisement(
        self,
        api_client,
        another_authorized_user,
        created_advertisement,
    ):
        payload = build_update_advertisement_payload(created_advertisement["image_url"])

        response = api_client.update_advertisement(
            another_authorized_user["token"],
            created_advertisement["id"],
            payload,
        )

        assert response.status_code == EXPECTED_STATUS_CODES["update_foreign_advertisement"]
        