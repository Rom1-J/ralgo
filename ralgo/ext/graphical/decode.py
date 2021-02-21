from typing import Union


class SquareDecoder:
    file: Union[str, bytes]
    is_bytes: bool

    def decode(self, file: Union[str, bytes], is_bytes: bool) -> str:
        self.file = file
        self.is_bytes = is_bytes

        raise NotImplementedError
