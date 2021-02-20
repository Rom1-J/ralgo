from typing import Union

import numpy as np
import sympy as sp

from ralgo.utils import encode_binary, clean_depth, clean_bits


class Encoder:
    message: str
    chars: tuple
    depth: int
    bits: int

    letters: np.ndarray
    output: str

    def __set_letters(self, message: str) -> None:
        letters = []

        for letter in message:
            letters.append(sp.factorint(ord(letter), multiple=True))

        self.letters = np.array(letters, dtype=object)

    def __get_depth(self) -> int:
        return max([len(i) for i in self.letters])

    def __get_bits(self) -> int:
        max_bits = np.amax(self.letters)
        return int(
            max_bits[0] if isinstance(max_bits, list) else max_bits
        ).bit_length()

    def __gen_key(self) -> None:
        self.output = (
            self.chars[0] * self.depth
            + self.chars[1] * self.bits
            + self.chars[0] * (self.bits + 1)
        )

    def __fill_letters(self) -> None:
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

    def __fill_random(self) -> None:
        self.output += (
            self.chars[1]
            + "".join(
                np.random.choice(self.chars, p=[0.8, 0.2])
                for _ in range(self.bits - 1)
            )
            + self.chars[0]
        )

    def __fill_words(self) -> np.ndarray:
        words, word = [], []

        for primes in self.letters:
            if np.prod(primes) != 1:
                word.append(primes)
            else:
                words.append(np.array(word, dtype=object))
                word = []

        words.append(np.array(word, dtype=object))

        return np.array(words, dtype=object)

    def __convert_layer(self, layer: np.ndarray) -> None:
        for element in layer:
            binary = encode_binary(np.binary_repr(element[0]), self.chars)
            output = (
                str(self.chars[0] * (self.bits + 1 - len(binary))) + binary
            )
            self.output += output

    def encode(
        self,
        message: Union[str, bytes],  # pylint: disable=unsubscriptable-object
        chars: tuple,
        depth: int,
        bits: int,
    ) -> str:
        self.message = message.replace(" ", chr(1))
        self.chars = chars

        self.__set_letters(self.message)

        self.depth = clean_depth(depth, self.__get_depth())
        self.bits = clean_bits(bits, self.__get_bits())

        self.__fill_letters()
        self.__gen_key()

        for word in self.__fill_words():
            layers = np.hsplit(word, self.depth)

            for layer in layers:
                self.__convert_layer(layer)

                self.__fill_random()
            self.output += (
                self.chars[1] + self.chars[0] * (self.bits - 1) + self.chars[1]
            )

        return self.output
