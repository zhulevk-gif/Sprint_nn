from data import EXPECTED_STATUS_CODES
from helpers import build_login_payload
from utils import extract_token, get_response_json


class TestLogin:
    def test_successful_login_of_registered_user(self, api_client, registered_user):
        payload = build_login_payload(registered_user)

        response = api_client.login_user(payload)
        response_json = get_response_json(response)

        assert response.status_code == EXPECTED_STATUS_CODES["login_success"]
        assert extract_token(response_json) is not None
        