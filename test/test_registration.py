from data import EXPECTED_STATUS_CODES
from helpers import build_registration_payload
from utils import extract_email, get_response_json


class TestRegistration:
    def test_successful_registration_with_unique_email(self, api_client):
        payload = build_registration_payload()

        response = api_client.register_user(payload)
        response_json = get_response_json(response)

        assert response.status_code == EXPECTED_STATUS_CODES["register_success"]
        assert extract_email(response_json) == payload["email"]

    def test_registration_with_existing_email(self, api_client, registered_user):
        response = api_client.register_user(registered_user)

        assert response.status_code == EXPECTED_STATUS_CODES["register_duplicate"]