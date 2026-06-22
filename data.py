from copy import deepcopy

from generators import generate_random_email

BASE_URL = "https://qa-desk.education-services.ru/api"
VERIFY_SSL = False
TIMEOUT = 15

REGISTER_ENDPOINT = "/signup"
LOGIN_ENDPOINT = "/signin"
CREATE_ADVERTISEMENT_ENDPOINT = "/create-listing"
UPDATE_ADVERTISEMENT_ENDPOINT = "/update-offer"
DELETE_ADVERTISEMENT_ENDPOINT = "/listings"

EXPECTED_STATUS_CODES = {
    "register_success": 201,
    "register_duplicate": 400,
    "login_success": 201,
    "create_advertisement_success": 201,
    "update_advertisement_success": 200,
    "update_foreign_advertisement": 401,
    "delete_advertisement_success": 200,
}

DEFAULT_PASSWORD = "123456Qq"

REGISTER_TEMPLATE = {
    "email": None,
    "password": DEFAULT_PASSWORD,
    "submitPassword": DEFAULT_PASSWORD,
}

LOGIN_TEMPLATE = {
    "email": None,
    "password": DEFAULT_PASSWORD,
}

ADVERTISEMENT_TEMPLATE = {
    "name": "wow",
    "category": "Книги",
    "condition": "Новый",
    "city": "Екатеринбург",
    "description": "wow wow wow",
    "price": 300,
}

UPDATED_ADVERTISEMENT_TEMPLATE = {
    "name": "wow",
    "category": "Книги",
    "condition": "Б/У",
    "city": "Нижний Новгород",
    "description": "wow wow wow aaaaa",
    "price": 300,
}


def get_registration_payload():
    payload = deepcopy(REGISTER_TEMPLATE)
    payload["email"] = generate_random_email()
    return payload


def get_login_payload(user_data):
    payload = deepcopy(LOGIN_TEMPLATE)
    payload["email"] = user_data["email"]
    return payload


def get_create_advertisement_payload():
    return deepcopy(ADVERTISEMENT_TEMPLATE)


def get_update_advertisement_payload(existing_image_url):
    payload = deepcopy(UPDATED_ADVERTISEMENT_TEMPLATE)
    payload["img1"] = existing_image_url
    payload["img2"] = "null"
    return payload