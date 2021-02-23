import os

from ralgo.ralgo import Ralgo


# def ratio(n: int, func) -> dict:
#     success = 0
#     fails = 0
#
#     for _ in range(n):
#         try:
#             func()
#             success += 1
#         except Exception as _:
#             fails += 1
#     return {"success": success, "fails": fails}


def test_convert_bytes():
    message = os.urandom(420)

    encoded = Ralgo(message).encode()
    global decoded
    decoded = encoded.decode()

    assert bytes(decoded) == message


# =======================
# =======================


def test_convert_image():
    with open("tests/bytes/image.png", "rb") as f:
        message = f.read()

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    print(type(decoded.statement), decoded.statement)
    print(message)

    assert bytes(decoded) == message


# =======================
# =======================


def test_convert_file():
    with open("tests/bytes/file.txt", "rb") as f:
        message = f.read()

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    print(type(decoded.statement), decoded.statement)
    print(message)

    assert bytes(decoded) == message
