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


def build_update_advertisement_payload(existing_image_url):
    payload = deepcopy(UPDATED_ADVERTISEMENT_TEMPLATE)
    payload["img1"] = existing_image_url
    return payload