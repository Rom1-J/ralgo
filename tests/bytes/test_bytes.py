import os

from ralgo.ralgo import Ralgo


def test_convert_bytes():
    message = os.urandom(420)

    encoded = Ralgo().encode(message)
    decoded = Ralgo().decode(encoded, is_bytes=True)

    assert decoded == message


def test_convert_image():
    with open('tests/bytes/image.png', 'rb') as f:
        message = f.read()

    encoded = Ralgo().encode(message)
    decoded = Ralgo().decode(encoded, is_bytes=True)

    assert decoded == message


def test_convert_file():
    with open('tests/bytes/file.txt', 'rb') as f:
        message = f.read()

    encoded = Ralgo().encode(message)
    decoded = Ralgo().decode(encoded, is_bytes=True)

    assert decoded == message
