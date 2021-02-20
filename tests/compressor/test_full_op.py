from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_decompress_basic():
    message = fake.text()

    encoded = Ralgo().encode(message)
    compressed = Ralgo().compress(encoded)

    decompressed = Ralgo().decompress(compressed)
    decoded = Ralgo().decode(decompressed)

    assert decoded == message
