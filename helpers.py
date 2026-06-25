from copy import deepcopy

from data import (
    ADVERTISEMENT_TEMPLATE,
    LOGIN_TEMPLATE,
    REGISTER_TEMPLATE,
    UPDATED_ADVERTISEMENT_TEMPLATE,
)
from generators import generate_random_email


def build_registration_payload():
    payload = deepcopy(REGISTER_TEMPLATE)
    payload["email"] = generate_random_email()
    return payload


def build_login_payload(user_data):
    payload = deepcopy(LOGIN_TEMPLATE)
    payload["email"] = user_data["email"]
    payload["password"] = user_data["password"]
    return payload


def build_create_advertisement_payload():
    return deepcopy(ADVERTISEMENT_TEMPLATE)


def build_update_advertisement_payload(existing_image_url=None):
    payload = deepcopy(UPDATED_ADVERTISEMENT_TEMPLATE)
    if existing_image_url is not None:
        payload["img1"] = existing_image_url
    return payload


def ensure_response_status(response, expected_status_code, error_text):
    if response.status_code != expected_status_code:
        raise RuntimeError(
            f"{error_text}. "
            f"Ожидался статус {expected_status_code}, "
            f"получен {response.status_code}. "
            f"Тело ответа: {response.text}"
        )
    