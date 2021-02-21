import itertools
from io import BytesIO

import numpy as np
from PIL import Image


class SquareEncoder:
    message: str
    chars: tuple

    output: bytes

    def __fill_random(self) -> None:
        self.message += "".join(
            np.random.choice(self.chars, p=[0.8, 0.2]) for _ in range(5)
        )

    def __char2color(self, char: str) -> list:
        if char == self.chars[0]:
            color = [
                np.random.randint(1, 42),
                np.random.randint(1, 42),
                np.random.randint(1, 42),
            ]
        else:
            color = [
                128 + np.random.randint(1, 42),
                128 + np.random.randint(1, 42),
                128 + np.random.randint(1, 42),
            ]

        return color

    def encode(self, message: str, chars: tuple) -> bytes:
        self.message = message
        self.chars = chars

        height, weight = (
            int(np.ceil(np.sqrt(len(self.message)))),
            int(np.ceil(np.sqrt(len(self.message)))),
        )

        array = np.zeros((height, weight, 3), dtype=np.uint8)
        i = 0

        for x, y in itertools.product(range(height), range(weight)):
            if i == len(self.message):
                self.__fill_random()
            else:
                array[x, y] = self.__char2color(self.message[i])
                i += 1

        with BytesIO() as output:
            Image.fromarray(array, "RGB").save(output, format="PNG")
            self.output = output.getvalue()

        return self.output
