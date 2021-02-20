from ralgo.exceptions import DecompressParseError
from ralgo.ralgo import Ralgo


def test_decompress_basic():
    message = "57{15}17162717211{12}112416172725121112271627133125181716242116111{14}17161726111511161"
    decoded = Ralgo().decompress(message)

    assert (
        decoded
        == ".....,,,,,,,...............,.......,......,,.......,.......,,.,............,.,,....,......,.......,,.......,,.....,..,.,..,,.......,......,,.......,...,,,.,,.....,........,.......,......,,....,,.,......,.,..............,.......,......,.......,,......,.,.....,.,......,"
    )

    # =======================

    message = "179111237161"
    decoded = Ralgo().decompress(message)

    assert decoded == ".,,,,,,,.........,.,..,,,.......,......,"


def test_decompress_fails():
    message = "*"

    try:
        _ = Ralgo().decompress(message)
        assert False
    except DecompressParseError as e:
        assert "Failed on parsing given compressed text" == e.message
