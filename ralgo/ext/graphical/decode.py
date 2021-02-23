import itertools
from io import BytesIO
from typing import Union

from PIL import Image

from ralgo.exceptions import InvalidArgument, InvalidImage


class SquareDecoder:
    file: Union[str, bytes]

    image: Image
    output: str

    def __load_file(self) -> tuple:
        if isinstance(self.file, str):
            self.image = Image.open(self.file)

            if self.image.size[0] == self.image.size[1]:
                return self.image.size

            raise InvalidImage(message="The given image has an invalid size")

        if isinstance(self.file, bytes):
            self.image = Image.open(BytesIO(self.file))

            return self.image.size

        raise InvalidArgument(
            message="The file must be given by path (str) or bytes (bytes)"
        )

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
