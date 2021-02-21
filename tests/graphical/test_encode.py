import math
import os

from PIL import Image
from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_encode_graphical_basic():
    message = "Salut"
    path = f"tests/graphical/tmp/{fake.pyint()}.png"

    encoded = Ralgo(message).encode().graphical().encode()

    encoded.save(path)

    img = Image.open(path)

    assert img.size == (17, 17)

    os.remove(path)

    # =======================

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
