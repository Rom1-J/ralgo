from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_compressor_full_op1():
    message = fake.text()

    encoded = Ralgo(message).encode()
    compressed = encoded.compress()

    decompressed = compressed.decompress()
    decoded = decompressed.decode()

    assert str(decoded) == message


def test_compressor_full_op2():
    message = fake.text()
    assert (
        str(Ralgo(message).encode().compress().decompress().decode())
        == message
    )
