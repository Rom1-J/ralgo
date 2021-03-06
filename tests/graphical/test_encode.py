import math
import os
from io import BytesIO

from PIL import Image
from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_encode_graphical_basic1():
    message = "Salut"

    _ = Ralgo(message).encode().graphical().encode()

    assert True  # this test should not fail


def test_encode_graphical_basic2():
    message = fake.text()

    encoded = Ralgo(message).encode()
    _ = encoded.graphical().encode()

    assert True  # this test should not fail


# =======================
# =======================


def test_encode_graphical_save1():
    message = "Salut"
    path = f"tests/graphical/tmp/{fake.pyint()}.png"

    encoded = Ralgo(message).encode().graphical().encode()

    encoded.save(path)

    img = Image.open(path)

    assert img.size == (17, 17)

    os.remove(path)


def test_encode_graphical_save2():
    message = fake.text()
    path = f"tests/graphical/tmp/{fake.pyint()}.png"

    encoded = Ralgo(message).encode()
    graphical = encoded.graphical().encode()

    graphical.save(path)

    img = Image.open(path)

    assert img.size == (
        math.ceil(math.sqrt(len(encoded))),
        math.ceil(math.sqrt(len(encoded))),
    )

    os.remove(path)


# =======================
# =======================


def test_encode_graphical_bytes1():
    message = "Salut"

    encoded = Ralgo(message).encode().graphical().encode()

    arr = encoded.to_bytes()

    img = Image.open(BytesIO(arr))

    assert img.size == (17, 17)


def test_encode_graphical_bytes2():
    message = fake.text()

    encoded = Ralgo(message).encode()
    graphical = encoded.graphical().encode()

    arr = graphical.to_bytes()

    img = Image.open(BytesIO(arr))

    assert img.size == (
        math.ceil(math.sqrt(len(encoded))),
        math.ceil(math.sqrt(len(encoded))),
    )
