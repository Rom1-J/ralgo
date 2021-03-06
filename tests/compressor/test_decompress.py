from ralgo.exceptions import DecompressParseError
from ralgo.ralgo import Ralgo


def test_decompress_basic1():
    message = "57{15}17162717211{12}112416172725121112271627133125181716242116111{14}17161726111511161"
    decoded = Ralgo(message).decompress()

    assert (
        str(decoded)
        == ".....,,,,,,,...............,.......,......,,.......,.......,,.,............,.,,....,......,.......,,.......,,.....,..,.,..,,.......,......,,.......,...,,,.,,.....,........,.......,......,,....,,.,......,.,..............,.......,......,.......,,......,.,.....,.,......,"
    )


def test_decompress_basic2():
    message = "179111237161"
    decoded = Ralgo(message).decompress()

    assert str(decoded) == ".,,,,,,,.........,.,..,,,.......,......,"


# =======================
# =======================


def test_decompress_fails():
    message = "*"

    try:
        _ = Ralgo(message).decompress()
        assert False
    except DecompressParseError as e:
        assert "Failed on parsing given compressed text" == e.message
