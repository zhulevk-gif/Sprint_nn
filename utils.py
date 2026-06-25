import base64


def get_response_json(response):
    try:
        return response.json()
    except ValueError:
        return {}


def _walk_path(data, path):
    current = data

    for key in path:
        if isinstance(key, int):
            if not isinstance(current, list):
                return None
            if key >= len(current):
                return None
            current = current[key]
            continue

        if not isinstance(current, dict):
            return None

        current = current.get(key)

    return current


def _extract_first(data, paths):
    for path in paths:
        value = _walk_path(data, path)
        if value is not None:
            return value
    return None


def extract_email(response_json):
    return _extract_first(
        response_json,
        (
            ("email",),
            ("user", "email"),
            ("data", "email"),
            ("data", "user", "email"),
        ),
    )


def extract_token(response_json):
    return _extract_first(
        response_json,
        (
            ("token", "access_token"),
            ("access_token", "access_token"),
            ("token",),
            ("accessToken",),
            ("access_token",),
            ("data", "token"),
            ("data", "access_token"),
        ),
    )


def extract_advertisement_id(response_json):
    return _extract_first(
        response_json,
        (
            ("id",),
            ("_id",),
            ("listingId",),
            ("advertisementId",),
            ("data", "id"),
            ("listing", "id"),
            ("advertisement", "id"),
        ),
    )


def extract_title(response_json):
    return _extract_first(
        response_json,
        (
            ("name",),
            ("title",),
            ("data", "name"),
            ("data", "title"),
            ("listing", "name"),
            ("advertisement", "name"),
        ),
    )


def extract_image_url(response_json):
    return _extract_first(
        response_json,
        (
            ("img1",),
            ("image",),
            ("images", 0),
            ("data", "img1"),
            ("listing", "img1"),
            ("advertisement", "img1"),
        ),
    )


def extract_message(response_json):
    return _extract_first(
        response_json,
        (
            ("message",),
            ("data", "message"),
        ),
    )


def get_test_image_file():
    image_bytes = base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+c9WQAAAAASUVORK5CYII="
    )
    return ("test_image.png", image_bytes, "image/png")
