from faker import Faker

from ralgo.exceptions import InvalidArgument, InvalidImage
from ralgo.ralgo import Ralgo

fake = Faker()


def test_decode_graphical_basic1():
    message = "Salut"

    encoded = Ralgo(message).encode().graphical().encode()
    decoded = Ralgo(encoded.decode()).decode()

    assert str(decoded) == message


def test_decode_graphical_basic2():
    message = fake.text()

    encoded = Ralgo(message).encode().graphical().encode()
    decoded = Ralgo(encoded.decode()).decode()

    assert str(decoded) == message


# =======================
# =======================


def test_decode_graphical_bytes1():
    with open("tests/graphical/files/qr.png", "rb") as f:
        qr = f.read()

    with open("tests/graphical/files/qr_encoded.png", "rb") as f:
        message = f.read()

    graphical = Ralgo(message).graphical().decode()
    output = Ralgo(graphical).decode()

    assert bytes(output) == qr


def test_decode_graphical_bytes2():
    with open("tests/graphical/files/file.txt", "rb") as f:
        file = f.read()

    with open("tests/graphical/files/file_encoded.png", "rb") as f:
        message = f.read()

    graphical = Ralgo(message).graphical()
    output = Ralgo(graphical.decode()).decode()

    assert bytes(output) == file


# =======================
# =======================


def test_decode_graphical_file1():
    with open("tests/graphical/files/qr.png", "rb") as f:
        qr = f.read()

    message = "tests/graphical/files/qr_encoded.png"

    graphical = Ralgo(message).graphical()
    output = Ralgo(graphical.decode()).decode()

    assert bytes(output) == qr


def test_decode_graphical_file2():
    with open("tests/graphical/files/file.txt", "rb") as f:
        file = f.read()

    message = "tests/graphical/files/file_encoded.png"

    graphical = Ralgo(message).graphical()
    output = Ralgo(graphical.decode()).decode()

    assert bytes(output) == file


# =======================
# =======================


def test_decode_graphical_fails1():
    try:
        # noinspection PyTypeChecker
        graphical = Ralgo(42).graphical()
        _ = Ralgo(graphical.decode()).decode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The file must be given by path (str) or bytes (bytes)"
        )


def test_decode_graphical_fails2():
    try:
        graphical = Ralgo("tests/graphical/files/42.jpeg").graphical()
        _ = Ralgo(graphical.decode()).decode()
        assert False
    except InvalidImage as e:
        assert e.message == "The given image has an invalid size"
