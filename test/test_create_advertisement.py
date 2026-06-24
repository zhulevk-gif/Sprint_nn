from data import EXPECTED_STATUS_CODES
from helpers import build_create_advertisement_payload
from utils import extract_advertisement_id, extract_title, get_response_json


class TestCreateAdvertisement:
    def test_successful_create_advertisement(self, api_client, authorized_user):
        payload = build_create_advertisement_payload()

        response = api_client.create_advertisement(authorized_user["token"], payload)
        response_json = get_response_json(response)

        assert response.status_code == EXPECTED_STATUS_CODES["create_advertisement_success"]
        assert extract_advertisement_id(response_json) is not None
        assert extract_title(response_json) == payload["name"]