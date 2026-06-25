import pytest

from api_client import ApiClient
from data import EXPECTED_STATUS_CODES
from helpers import (
    build_create_advertisement_payload,
    build_login_payload,
    build_registration_payload,
    ensure_response_status,
)
from utils import (
    extract_advertisement_id,
    extract_image_url,
    extract_token,
    get_response_json,
)


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def registered_user(api_client):
    user_data = build_registration_payload()
    response = api_client.register_user(user_data)

    ensure_response_status(
        response,
        EXPECTED_STATUS_CODES["register_success"],
        "Не удалось зарегистрировать пользователя",
    )

    return user_data


@pytest.fixture
def authorized_user(api_client, registered_user):
    response = api_client.login_user(build_login_payload(registered_user))
    response_json = get_response_json(response)
    token = extract_token(response_json)

    ensure_response_status(
        response,
        EXPECTED_STATUS_CODES["login_success"],
        "Не удалось авторизовать пользователя",
    )

    if token is None:
        raise RuntimeError("В ответе на авторизацию отсутствует токен")

    return {
        "user_data": registered_user,
        "token": token,
    }


@pytest.fixture
def another_authorized_user(api_client):
    user_data = build_registration_payload()
    register_response = api_client.register_user(user_data)

    ensure_response_status(
        register_response,
        EXPECTED_STATUS_CODES["register_success"],
        "Не удалось зарегистрировать второго пользователя",
    )

    login_response = api_client.login_user(build_login_payload(user_data))
    login_response_json = get_response_json(login_response)
    token = extract_token(login_response_json)

    ensure_response_status(
        login_response,
        EXPECTED_STATUS_CODES["login_success"],
        "Не удалось авторизовать второго пользователя",
    )

    if token is None:
        raise RuntimeError("В ответе на авторизацию второго пользователя отсутствует токен")

    return {
        "user_data": user_data,
        "token": token,
    }


@pytest.fixture
def created_advertisement(api_client, authorized_user):
    payload = build_create_advertisement_payload()
    response = api_client.create_advertisement(authorized_user["token"], payload)
    response_json = get_response_json(response)
    advertisement_id = extract_advertisement_id(response_json)
    image_url = extract_image_url(response_json)

    ensure_response_status(
        response,
        EXPECTED_STATUS_CODES["create_advertisement_success"],
        "Не удалось создать объявление",
    )

    if advertisement_id is None:
        raise RuntimeError("В ответе на создание объявления отсутствует id")

    if image_url is None:
        image_url = payload.get("img1")

    return {
        "id": advertisement_id,
        "image_url": image_url,
        "payload": payload,
        "owner": authorized_user,
    }
