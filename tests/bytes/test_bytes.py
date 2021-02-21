import os

from ralgo.ralgo import Ralgo


def test_convert_bytes():
    message = os.urandom(420)

    encoded = Ralgo(message).encode()
    decoded = encoded.decode(is_bytes=True)

    assert bytes(decoded) == message


def test_convert_image():
    with open("tests/bytes/image.png", "rb") as f:
        message = f.read()

    encoded = Ralgo(message).encode()
    decoded = encoded.decode(is_bytes=True)

    assert bytes(decoded) == message


def test_convert_file():
    with open("tests/bytes/file.txt", "rb") as f:
        message = f.read()

    encoded = Ralgo(message).encode()
    decoded = encoded.decode(is_bytes=True)

    assert bytes(decoded) == message
