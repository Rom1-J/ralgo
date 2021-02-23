from typing import Union

from ralgo.decode import Decoder
from ralgo.encode import Encoder
from ralgo.ext import compressor
from ralgo.ext.graphical.square import Square


class Ralgo(Encoder, Decoder, Square):
    statement: Union[str, bytes, "Ralgo"]

    # noinspection PyMissingConstructor
    def __init__(
        self,
        statement: Union[str, bytes, "Ralgo", Square],
    ):
        if isinstance(statement, (Ralgo, Square)):
            self.statement = statement.statement
        else:
            self.statement = statement

    def __str__(self):
        return self.statement

    def __bytes__(self):
        return self.statement

    def __len__(self):
        return len(self.statement)

    def encode(
        self,
        chars: tuple = (".", ","),
        depth: int = None,
        bits: int = None,
    ) -> "Ralgo":
        self.statement = super().encode(
            message=self.statement, chars=chars, depth=depth, bits=bits
        )

        return self

    def decode(
        self,
        chars: tuple = (".", ","),
        depth: int = None,
        bits: int = None,
    ) -> "Ralgo":
        self.statement = super().decode(
            message=self.statement,
            chars=chars,
            depth=depth,
            bits=bits,
        )

        return self

    def compress(self) -> "Ralgo":
        self.statement = compressor.Compress().compress(self.statement)

        return self

    def decompress(self) -> "Ralgo":
        self.statement = compressor.Decompress().decompress(
            str(self.statement)
        )

        return self

    def graphical(self) -> Square:
        return Square(statement=self.statement)
