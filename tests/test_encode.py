from faker import Faker

from ralgo.ralgo import Ralgo
from ralgo.exceptions import DepthError, BitsError, InvalidArgument
from tests.asserts import contains_only

fake = Faker()


def test_encode_basic():
    message = "s"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 43

    # =======================

    message = "S"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 40

    # =======================

    message = "Salut"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 268


def test_encode_chars():
    message = fake.text()

    encoded = Ralgo(message).encode()

    assert contains_only(str(encoded), (".", ","))

    # =======================

    message = fake.text()
    chars = ("*", "-")

    encoded = Ralgo(message).encode(chars=chars)

    assert contains_only(str(encoded), chars)

    # =======================

    message = fake.text()
    chars = ("-", "—")

    encoded = Ralgo(message).encode(chars=chars)

    assert contains_only(str(encoded), chars)


def test_encode_depth():
    message = "Salut"

    encoded = Ralgo(message).encode(depth=9)

    assert str(encoded)[:10] == "." * 9 + ","

    # =======================

    message = "Salut"

    try:
        _ = Ralgo(message).encode(depth=1)
        assert False
    except DepthError as e:
        assert "Given depth is too low" == e.message

    # =======================

    message = "Salut"

    try:
        # noinspection PyTypeChecker
        _ = Ralgo(message).encode(depth="fail")
        assert False
    except DepthError as e:
        assert "Given depth must be an int" == e.message


def test_encode_bits():
    message = "Salut"

    encoded = Ralgo(message).encode(depth=7, bits=9)

    assert str(encoded)[:16] == "." * 7 + "," * 9

    # =======================

    message = "Salut"

    try:
        _ = Ralgo(message).encode(depth=7, bits=1)
        assert False
    except BitsError as e:
        assert "Given bits is too low" == e.message

    # =======================

    message = "Salut"

    try:
        # noinspection PyTypeChecker
        _ = Ralgo(message).encode(depth=7, bits="fail")
        assert False
    except BitsError as e:
        assert "Given bits must be an int" == e.message


def test_encode_fails():
    try:
        # noinspection PyTypeChecker
        _ = Ralgo({3}).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )

    # =======================

    try:
        # noinspection PyTypeChecker
        _ = Ralgo([42]).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )

    # =======================

    try:
        # noinspection PyTypeChecker
        _ = Ralgo(bytearray(5)).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )
