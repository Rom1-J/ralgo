from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_decode_graphical_basic():
    message = "Salut"

    encoded = Ralgo(message).encode().graphical().encode()
    decoded = Ralgo(str(encoded.decode())).decode()

    assert str(decoded) == message

    # =======================

    message = fake.text()

    encoded = Ralgo(message).encode().graphical().encode()
    decoded = Ralgo(str(encoded.decode())).decode()

    assert str(decoded) == message


def test_decode_graphical_bytes():
    with open("tests/graphical/files/qr.png", "rb") as f:
        qr = f.read()

    with open("tests/graphical/files/qr_encoded.png", "rb") as f:
        message = f.read()

    graphical = Ralgo(message).graphical()
    output = Ralgo(str(graphical.decode())).decode(is_bytes=True)

    assert bytes(output) == qr

    # =======================

    with open("tests/graphical/files/file.txt", "rb") as f:
        file = f.read()

    with open("tests/graphical/files/file_encoded.png", "rb") as f:
        message = f.read()

    graphical = Ralgo(message).graphical()
    output = Ralgo(str(graphical.decode())).decode(is_bytes=True)

    assert bytes(output) == file


def test_decode_graphical_file():
    with open("tests/graphical/files/qr.png", "rb") as f:
        qr = f.read()

    message = "tests/graphical/files/qr_encoded.png"

    graphical = Ralgo(message).graphical()
    output = Ralgo(str(graphical.decode())).decode(is_bytes=True)

    assert bytes(output) == qr

    # =======================

    with open("tests/graphical/files/file.txt", "rb") as f:
        file = f.read()

    message = "tests/graphical/files/file_encoded.png"

    graphical = Ralgo(message).graphical()
    output = Ralgo(str(graphical.decode())).decode(is_bytes=True)

    assert bytes(output) == file


def test_decode_graphical_fails():
    try:
        # noinspection PyTypeChecker
        graphical = Ralgo(42).graphical()
        _ = Ralgo(str(graphical.decode())).decode(is_bytes=True)
        assert False
    except NotImplementedError:
        assert True
