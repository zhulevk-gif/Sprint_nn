from data import EXPECTED_STATUS_CODES
from utils import extract_message, get_response_json


class TestDeleteAdvertisement:
    def test_successful_delete_advertisement(
        self,
        api_client,
        authorized_user,
        created_advertisement,
    ):
        response = api_client.delete_advertisement(
            authorized_user["token"],
            created_advertisement["id"],
        )
        response_json = get_response_json(response)

        assert response.status_code == EXPECTED_STATUS_CODES["delete_advertisement_success"]
        assert extract_message(response_json) == "Объявление удалено успешно"