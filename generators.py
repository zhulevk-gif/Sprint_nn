import uuid


def generate_random_email():
    return f"autotest_{uuid.uuid4().hex[:12]}@yandex.ru"