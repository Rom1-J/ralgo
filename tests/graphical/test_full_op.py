import os

from faker import Faker

from ralgo.ralgo import Ralgo

fake = Faker()


def test_graphical_full_op():
    message = fake.text()

    encoded = Ralgo(message).encode()
    graphical = encoded.graphical().encode()

    arr = graphical.to_bytes()
    decoded_graphical = Ralgo(arr).graphical().decode()

    decoded = Ralgo(decoded_graphical).decode()

    assert str(decoded) == message


# =======================
# =======================


def test_graphical_full_op_file1():
    path = f"tests/graphical/tmp/{fake.pyint()}.png"

    with open("tests/graphical/files/qr.png", "rb") as f:
        message = f.read()

    Ralgo(message).encode().graphical().encode().save(path)

    output = Ralgo(Ralgo(path).graphical().decode()).decode()

    assert bytes(output) == message

    os.remove(path)


def test_graphical_full_op_file2():
    path = f"tests/graphical/tmp/{fake.pyint()}.png"

    with open("tests/graphical/files/file.txt", "rb") as f:
        message = f.read()

    Ralgo(message).encode().graphical().encode().save(path)

    output = Ralgo(Ralgo(path).graphical().decode()).decode()

    assert bytes(output) == message

    os.remove(path)
