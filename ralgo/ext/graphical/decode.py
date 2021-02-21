import itertools
from io import BytesIO
from typing import Union, NoReturn

from PIL import Image


class SquareDecoder:
    file: Union[str, bytes]

    image: Image
    output: str

    def __load_file(self) -> Union[tuple, NoReturn]:
        if isinstance(self.file, str):
            self.image = Image.open(self.file)
            return self.image.size
        if isinstance(self.file, bytes):
            self.image = Image.open(BytesIO(self.file))
            return self.image.size

        raise NotImplementedError

    @staticmethod
    def __color2char(color):
        if sum(color) > 128:
            return ","
        return "."

    def decode(self, file: Union[str, bytes]) -> str:
        self.file = file

        height, weight = self.__load_file()

        self.output = ""

        for x, y in itertools.product(range(height), range(weight)):
            if sum(self.image.getpixel((y, x))) == 0:
                break

            self.output += self.__color2char(self.image.getpixel((y, x)))

        return self.output
