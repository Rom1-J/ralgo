from io import BytesIO
from typing import Union

from PIL import Image

from ralgo.ext.graphical.decode import SquareDecoder
from ralgo.ext.graphical.encode import SquareEncoder


class Square(SquareEncoder, SquareDecoder):
    statement: Union[str, bytes, "Square"]

    def __init__(
        self,
        statement: Union[str, bytes, "Square"],
    ):
        self.statement = statement

    def __str__(self):
        return self.statement

    def encode(
        self,
        chars: tuple = (".", ","),
    ) -> "Square":
        self.statement = super().encode(message=self.statement, chars=chars)

        return self

    def decode(
        self,
    ) -> "Square":
        self.statement = super().decode(file=self.statement)

        return self

    def to_bytes(self) -> bytes:
        return self.statement

    def save(self, path: str) -> "SquareEncoder":
        image = Image.open(BytesIO(self.statement))
        image.save(path)

        return self
