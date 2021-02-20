class Decoder:
    message: str
    chars: tuple
    depth: int
    bits: int

    def decode(self, message: str, chars: tuple, depth: int, bits: int) -> str:
        self.message = message
        self.chars = chars
        self.depth = depth
        self.bits = bits

        raise NotImplementedError
