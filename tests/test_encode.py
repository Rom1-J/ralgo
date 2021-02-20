from faker import Faker

from ralgo.ralgo import Ralgo
from ralgo.exceptions import DepthError
from tests.asserts import contains_only

fake = Faker()


def test_encode_basic():
    message = "s"
    encoded = Ralgo().encode(message)

    assert len(encoded) == 43

    # =======================

    message = "S"
    encoded = Ralgo().encode(message)

    assert len(encoded) == 40

    # =======================

    message = "Salut"
    encoded = Ralgo().encode(message)

    assert len(encoded) == 268


def test_encode_chars():
    message = fake.text()

    encoded = Ralgo().encode(message)

    assert contains_only(encoded, (".", ","))

    # =======================

    message = fake.text()
    chars = ("*", "-")

    encoded = Ralgo().encode(message, chars=chars)

    assert contains_only(encoded, chars)

    # =======================

    message = fake.text()
    chars = ("-", "—")

    encoded = Ralgo().encode(message, chars=chars)

    assert contains_only(encoded, chars)


def test_encode_depth():
    message = "Salut"

    encoded = Ralgo().encode(message, depth=9)

    assert encoded[:10] == "." * 9 + ","

    # =======================

    message = "Salut"

    try:
        _ = Ralgo().encode(message, depth=1)
        assert False
    except DepthError as e:
        assert "Given depth is too low" == e.message

    # =======================

    message = "Salut"

    try:
        _ = Ralgo().encode(message, depth="fail")
        assert False
    except DepthError as e:
        assert "Given depth must be an int" == e.message
