from faker import Faker

from ralgo.ralgo import Ralgo
from ralgo.exceptions import DecodeError, CharsError

fake = Faker()


def test_decode_basic1():
    message = ".....,,,,,,,...............,.......,......,,.......,.......,,.,............,.,,....,......,.......,,.......,,.....,..,.,..,,.......,......,,.......,...,,,.,,.....,........,.......,......,,....,,.,......,.,..............,.......,......,.......,,......,.,.....,.,......,"
    decoded = Ralgo(message).decode()

    assert str(decoded) == "Salut"


def test_decode_basic2():
    message = ".,,,,,,,.........,.,..,,,.......,......,"
    decoded = Ralgo(message).decode()

    assert str(decoded) == "S"


def test_decode_basic3():
    message = fake.text()

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    assert str(decoded) == message


def test_decode_basic4():
    message = "slt"

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    assert str(decoded) == message


# =======================
# =======================


def test_decode_chars1():
    message = "*****-------***************-*******-******--*******-*******--*-************-*--****-******-*******--*******--*****-**-*-**--*******-******--*******-***---*--*****-********-*******-******--****--*-******-*-**************-*******-******-*******--******-*-*****-*-******-"
    chars = ("*", "-")
    decoded = Ralgo(message).decode(chars=chars)

    assert str(decoded) == "Salut"


def test_decode_chars2():
    message = "0111111100000000010100111000000010000001"
    chars = ("0", "1")
    decoded = Ralgo(message).decode(chars=chars)

    assert str(decoded) == "S"


def test_decode_chars3():
    message = fake.text()
    chars = ("-", "—")

    encoded = Ralgo(message).encode(chars=chars)
    decoded = encoded.decode(chars=chars)

    assert str(decoded) == message


def test_decode_chars4():
    message = "1" * 42
    chars = ("1", "1")

    try:
        _ = Ralgo(message).encode(chars=chars)
        assert False
    except CharsError as e:
        assert "Given chars must not be the same" == e.message


# =======================
# =======================


def test_decode_depth1():
    message = ".........,,,,,,,...............,.......,......,,.......,......,.,....,.........,.,,....,......,,.......,.......,,....,.........,.......,.......,.......,.......,,,.,..,........,.......,......,.......,,.......,,,.............,.......,.......,....,,.,...,,,.,,..............,.......,......,.......,,.......,,....,.........,.......,.......,.......,.......,,,.,.....,.,..,,.......,.......,.......,......,.,.....,........,.......,......,,.......,.......,,.......,......,"

    decoded = Ralgo(message).decode(depth=9)

    assert str(decoded) == "Salut"


def test_decode_depth2():
    message = ".,,,,,,,...............,.......,......,,.......,......,.,....,.........,.,,....,......,,.......,.......,,....,.........,.......,.......,.......,.......,,,.,..,........,.......,......,.......,,.......,,,.............,.......,.......,....,,.,...,,,.,,..............,.......,......,.......,,.......,,....,.........,.......,.......,.......,.......,,,.,.....,.,..,,.......,.......,.......,......,.,.....,........,.......,......,,.......,.......,,.......,......,"

    try:
        _ = Ralgo(message).decode()
        assert False
    except DecodeError as e:
        assert "Failed to decode one layer" == e.message


def test_decode_depth3():
    message = fake.text()
    depth = 12

    encoded = Ralgo(message).encode(depth=depth)
    decoded = encoded.decode(depth=depth)

    assert str(decoded) == message


# =======================
# =======================


def test_decode_bits1():
    message = ".......,,,,,,,,,...................,.........,.........,........,,........,.,......,...........,.........,........,..........,.....,,,.,,..................,.........,........,.........,,.........,,....,.............,.........,........,,.........,........,.,............,.,..,,.........,........,,.........,.........,,.......,..........,.........,.........,.........,.........,,,....,............,...,,....,........,,......,,.,.........,,..,....,.,........,"

    decoded = Ralgo(message).decode(depth=7, bits=9)

    print(decoded, type(decoded), decoded.statement, type(decoded.statement))

    assert str(decoded) == "Salut"


def test_decode_bits2():
    message = ".......,,,,,,,,...................,.........,.........,........,,........,.,......,...........,.........,........,..........,.....,,,.,,..................,.........,........,.........,,.........,,....,.............,.........,........,,.........,........,.,............,.,..,,.........,........,,.........,.........,,.......,..........,.........,.........,.........,.........,,,....,............,...,,....,........,,......,,.,.........,,..,....,.,........,"

    decoded = Ralgo(message).decode()

    assert str(decoded) == ""


def test_decode_bits3():
    message = fake.text()
    depth = 12
    bits = 42

    encoded = Ralgo(message).encode(depth=depth, bits=bits)
    decoded = encoded.decode(depth=depth, bits=bits)

    assert str(decoded) == message


# =======================
# =======================


def test_decode_fake_bytes1():
    message = "b'ezfez"

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    assert str(decoded) == message


def test_decode_fake_bytes4():
    message = "b'ezf'ez'"

    encoded = Ralgo(message).encode()
    decoded = encoded.decode()

    assert str(decoded) == message
