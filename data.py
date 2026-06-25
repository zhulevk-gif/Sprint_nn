DEFAULT_USER_NAME = "Konstantin"
DEFAULT_PASSWORD = "QaDesk123!"

REGISTER_TEMPLATE = {
    "name": DEFAULT_USER_NAME,
    "email": "",
    "password": DEFAULT_PASSWORD,
}

LOGIN_TEMPLATE = {
    "email": "",
    "password": DEFAULT_PASSWORD,
}

ADVERTISEMENT_TEMPLATE = {
    "name": "wow",
    "category": "Книги",
    "condition": "Новое",
    "city": "Екатеринбург",
    "description": "wow wow wow",
    "price": 300,
}

UPDATED_ADVERTISEMENT_TEMPLATE = {
    "name": "updated wow",
    "category": "Книги",
    "condition": "Б/У",
    "city": "Нижний Новгород",
    "description": "wow wow wow aaaaa",
    "price": 300,
}

EXPECTED_STATUS_CODES = {
    "register_success": 201,
    "register_duplicate": 400,
    "login_success": 201,
    "create_advertisement_success": 201,
    "update_advertisement_success": 200,
    "update_foreign_advertisement": 401,
    "delete_advertisement_success": 200,
}

EXPECTED_MESSAGES = {
    "delete_advertisement_success": "Объявление удалено успешно",
}
