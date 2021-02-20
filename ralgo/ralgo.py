from ralgo.decoder import Decoder
from ralgo.encoder import Encoder


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
