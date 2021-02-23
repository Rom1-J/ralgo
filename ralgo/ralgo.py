from typing import Union, Optional

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
        depth: Optional[int] = None,
        bits: Optional[int] = None,
    ) -> "Ralgo":
        self.statement = super()._encode(
            message=self.statement, chars=chars, depth=depth, bits=bits
        )

        return self

    def decode(
        self,
        chars: tuple = (".", ","),
        depth: Optional[int] = None,
        bits: Optional[int] = None,
    ) -> "Ralgo":
        self.statement = super()._decode(
            message=str(self.statement),  # assuming the statement as a string
            chars=chars,
            depth=depth,
            bits=bits,
        )

        return self

    def compress(self) -> "Ralgo":
        """Compress

        Function called when we want the output as compressed

        Returns
        -------
        Ralgo
           Main instance
        """
        self.statement = compressor.Compress().compress(self.statement)

        return self

    def decompress(self) -> "Ralgo":
        """Decompress

        Function called when we want the output as decompressed

        Returns
        -------
        Ralgo
           Main instance
        """
        self.statement = compressor.Decompress().decompress(
            str(self.statement)
        )

        return self

    def graphical(self) -> Square:
        """Graphical

        Function called when we want the output as graphical

        Returns
        -------
        Square
           Square instance
        """
        return Square(statement=self.statement)
