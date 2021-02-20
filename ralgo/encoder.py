from typing import NoReturn, Union

import numpy as np
import sympy as sp

from ralgo.exceptions import DepthError, BitsError
from ralgo.utils import encode_binary


class Encoder:
    message: str
    chars: tuple
    depth: int
    bits: int

    letters: np.ndarray
    output: str

    def _set_letters(self, message: str) -> None:
        letters = []

        for letter in message:
            letters.append(sp.factorint(ord(letter), multiple=True))

        self.letters = np.array(letters, dtype=object)

    def _get_depth(self) -> int:
        return max([len(i) for i in self.letters])

    def _get_bits(self) -> int:
        max_bits = np.amax(self.letters)
        return int(
            max_bits[0] if isinstance(max_bits, list) else max_bits
        ).bit_length()

    def _gen_key(self) -> None:
        self.output = (
            self.chars[0] * self.depth
            + self.chars[1] * self.bits
            + self.chars[0] * (self.bits + 1)
        )

    def _fill_letters(self) -> None:
        letters = []

        for primes in self.letters:
            if len(primes) == self.depth:
                np.random.shuffle(primes)
                letters.append(primes)
            else:
                primes = [1 for _ in range(self.depth - len(primes))] + list(
                    primes
                )

                np.random.shuffle(primes)
                letters.append(primes)

        self.letters = np.array(letters, dtype=object)

    def _fill_random(self) -> None:
        self.output += (
            self.chars[1]
            + "".join(
                np.random.choice(self.chars, p=[0.8, 0.2])
                for _ in range(self.bits - 1)
            )
            + self.chars[0]
        )

    def _fill_words(self) -> np.ndarray:
        words, word = [], []

        for primes in self.letters:
            if np.prod(primes) != 1:
                word.append(primes)
            else:
                words.append(np.array(word, dtype=object))
                word = []

        words.append(np.array(word, dtype=object))

        return np.array(words, dtype=object)

    def _clean_depth(
        self, depth: int
    ) -> Union[NoReturn, bool]:  # pylint: disable=unsubscriptable-object
        if not isinstance(depth, int):
            raise DepthError(message="Given depth must be an int")
        if self._get_depth() > depth:
            raise DepthError(message="Given depth is too low")

        return True

    def _clean_bits(
        self, bits: int
    ) -> Union[NoReturn, bool]:  # pylint: disable=unsubscriptable-object
        if not isinstance(bits, int):
            raise BitsError(message="Given bits must be an int")
        if self._get_depth() > bits:
            raise BitsError(message="Given bits is too low")

        return True

    def _convert_layer(self, layer: np.ndarray) -> None:
        for element in layer:
            binary = encode_binary(np.binary_repr(element[0]), self.chars)
            output = (
                str(self.chars[0] * (self.bits + 1 - len(binary))) + binary
            )
            self.output += output

    def encode(self, message: str, chars: tuple, depth: int, bits: int) -> str:
        self.message = message.replace(" ", chr(1))
        self.chars = chars

        self._set_letters(self.message)

        if not depth:
            self.depth = self._get_depth()
        elif self._clean_depth(depth):
            self.depth = depth

        if not bits:
            self.bits = self._get_bits()
        elif self._clean_bits(bits):
            self.bits = bits

        self._fill_letters()
        self._gen_key()

        for word in self._fill_words():
            layers = np.hsplit(word, self.depth)

            for layer in layers:
                self._convert_layer(layer)

                self._fill_random()
            self.output += (
                self.chars[1] + self.chars[0] * (self.bits - 1) + self.chars[1]
            )

        return self.output
