from faker import Faker

from ralgo.ralgo import Ralgo
from ralgo.exceptions import DepthError, BitsError, InvalidArgument, CharsError
from tests.asserts import contains_only

fake = Faker()


def test_encode_basic1():
    message = "s"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 43


def test_encode_basic2():
    message = "S"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 40


def test_encode_basic3():
    message = "Salut"
    encoded = Ralgo(message).encode()

    assert len(encoded) == 268


def test_encode_basic4():
    message = fake.text()
    _ = Ralgo(message).encode()

    assert True


# =======================
# =======================


def test_encode_chars1():
    message = fake.text()

    encoded = Ralgo(message).encode()

    assert contains_only(str(encoded), (".", ","))


def test_encode_chars2():
    message = fake.text()
    chars = ("*", "-")

    encoded = Ralgo(message).encode(chars=chars)

    assert contains_only(str(encoded), chars)


def test_encode_chars3():
    message = fake.text()
    chars = ("-", "—")

    encoded = Ralgo(message).encode(chars=chars)

    assert contains_only(str(encoded), chars)


def test_encode_chars4():
    message = fake.text()
    chars = ("1", "1")

    try:
        _ = Ralgo(message).encode(chars=chars)
        assert False
    except CharsError as e:
        assert "Given chars must not be the same" == e.message


# =======================
# =======================


def test_encode_depth1():
    message = "Salut"

    encoded = Ralgo(message).encode(depth=9)

    assert str(encoded)[:10] == "." * 9 + ","


def test_encode_depth2():
    message = "Salut"

    try:
        _ = Ralgo(message).encode(depth=1)
        assert False
    except DepthError as e:
        assert "Given depth is too low" == e.message


def test_encode_depth3():
    message = "Salut"

    try:
        # noinspection PyTypeChecker
        _ = Ralgo(message).encode(depth="fail")
        assert False
    except DepthError as e:
        assert "Given depth must be an int" == e.message


# =======================
# =======================


def test_encode_bits1():
    message = "Salut"

    encoded = Ralgo(message).encode(depth=7, bits=9)

    assert str(encoded)[:16] == "." * 7 + "," * 9


def test_encode_bits2():
    message = "Salut"

    try:
        _ = Ralgo(message).encode(depth=7, bits=1)
        assert False
    except BitsError as e:
        assert "Given bits is too low" == e.message


def test_encode_bits3():
    message = "Salut"

    try:
        # noinspection PyTypeChecker
        _ = Ralgo(message).encode(depth=7, bits="fail")
        assert False
    except BitsError as e:
        assert "Given bits must be an int" == e.message


# =======================
# =======================


def test_encode_fails1():
    try:
        # noinspection PyTypeChecker
        _ = Ralgo({3}).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )


def test_encode_fails2():
    try:
        # noinspection PyTypeChecker
        _ = Ralgo([42]).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )


def test_encode_fails3():
    try:
        # noinspection PyTypeChecker
        _ = Ralgo(bytearray(5)).encode()
        assert False
    except InvalidArgument as e:
        assert (
            e.message
            == "The data to work with must be of type str, int, float or bytes"
        )
