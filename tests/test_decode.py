from faker import Faker

from ralgo.ralgo import Ralgo
from ralgo.exceptions import DepthError, BitsError, DecodeError

fake = Faker()


def test_decode_basic():
    message = ".....,,,,,,,...............,.......,......,,.......,.......,,.,............,.,,....,......,.......,,.......,,.....,..,.,..,,.......,......,,.......,...,,,.,,.....,........,.......,......,,....,,.,......,.,..............,.......,......,.......,,......,.,.....,.,......,"
    decoded = Ralgo().decode(message)

    assert decoded == "Salut"

    # =======================

    message = ".,,,,,,,.........,.,..,,,.......,......,"
    decoded = Ralgo().decode(message)

    assert decoded == "S"

    # =======================

    message = fake.text()
    encoded = Ralgo().encode(message)

    assert message == Ralgo().decode(encoded)


def test_decode_chars():
    message = "*****-------***************-*******-******--*******-*******--*-************-*--****-******-*******--*******--*****-**-*-**--*******-******--*******-***---*--*****-********-*******-******--****--*-******-*-**************-*******-******-*******--******-*-*****-*-******-"
    chars = ("*", "-")
    decoded = Ralgo().decode(message, chars=chars)

    assert decoded == "Salut"

    # =======================

    message = "0111111100000000010100111000000010000001"
    chars = ("0", "1")
    decoded = Ralgo().decode(message, chars=chars)

    assert decoded == "S"

    # =======================

    message = fake.text()
    chars = ("-", "—")
    encoded = Ralgo().encode(message, chars=chars)

    assert message == Ralgo().decode(encoded, chars=chars)


def test_decode_depth():
    message = ".........,,,,,,,...............,.......,......,,.......,......,.,....,.........,.,,....,......,,.......,.......,,....,.........,.......,.......,.......,.......,,,.,..,........,.......,......,.......,,.......,,,.............,.......,.......,....,,.,...,,,.,,..............,.......,......,.......,,.......,,....,.........,.......,.......,.......,.......,,,.,.....,.,..,,.......,.......,.......,......,.,.....,........,.......,......,,.......,.......,,.......,......,"

    decoded = Ralgo().decode(message, depth=9)

    assert decoded == "Salut"

    # =======================

    message = ".,,,,,,,...............,.......,......,,.......,......,.,....,.........,.,,....,......,,.......,.......,,....,.........,.......,.......,.......,.......,,,.,..,........,.......,......,.......,,.......,,,.............,.......,.......,....,,.,...,,,.,,..............,.......,......,.......,,.......,,....,.........,.......,.......,.......,.......,,,.,.....,.,..,,.......,.......,.......,......,.,.....,........,.......,......,,.......,.......,,.......,......,"

    try:
        _ = Ralgo().decode(message)
        assert False
    except DecodeError as e:
        assert "Failed to decode one layer" == e.message

    # =======================

    message = fake.text()
    depth = 12
    encoded = Ralgo().encode(message, depth=depth)

    assert message == Ralgo().decode(encoded, depth=depth)


def test_decode_bits():
    message = ".......,,,,,,,,,...................,.........,.........,........,,........,.,......,...........,.........,........,..........,.....,,,.,,..................,.........,........,.........,,.........,,....,.............,.........,........,,.........,........,.,............,.,..,,.........,........,,.........,.........,,.......,..........,.........,.........,.........,.........,,,....,............,...,,....,........,,......,,.,.........,,..,....,.,........,"

    decoded = Ralgo().decode(message, depth=7, bits=9)

    assert decoded == "Salut"

    # =======================

    message = ".......,,,,,,,,...................,.........,.........,........,,........,.,......,...........,.........,........,..........,.....,,,.,,..................,.........,........,.........,,.........,,....,.............,.........,........,,.........,........,.,............,.,..,,.........,........,,.........,.........,,.......,..........,.........,.........,.........,.........,,,....,............,...,,....,........,,......,,.,.........,,..,....,.,........,"

    decoded = Ralgo().decode(message)

    assert decoded == ""

    # =======================

    message = fake.text()
    depth = 12
    bits = 42
    encoded = Ralgo().encode(message, depth=depth, bits=bits)

    assert message == Ralgo().decode(encoded, depth=depth, bits=bits)