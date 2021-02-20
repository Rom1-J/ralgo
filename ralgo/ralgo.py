from ralgo.decoder import Decoder
from ralgo.encoder import Encoder
from ralgo.ext import compressor


class Ralgo(Encoder, Decoder):
    def encode(
        self,
        message: str,
        chars: tuple = (".", ","),
        depth: int = None,
        bits: int = None,
    ) -> str:
        return super().encode(
            message=message, chars=chars, depth=depth, bits=bits
        )

    def decode(
        self,
        message: str,
        chars: tuple = (".", ","),
        depth: int = None,
        bits: int = None,
    ) -> str:
        return super().decode(
            message=message, chars=chars, depth=depth, bits=bits
        )

    @staticmethod
    def compress(message: str) -> str:
        return compressor.Compress().compress(message)

    @staticmethod
    def decompress(message: str) -> str:
        return compressor.Decompress().decompress(message)
