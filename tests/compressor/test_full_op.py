from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_decompress_basic():
    message = fake.text()

    encoded = Ralgo(message).encode()
    compressed = encoded.compress()

    decompressed = compressed.decompress()
    decoded = decompressed.decode()

    assert str(decoded) == message

    assert (
        str(Ralgo(message).encode().compress().decompress().decode())
        == message
    )
