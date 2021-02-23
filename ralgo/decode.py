import ast
import re
from typing import Union

import numpy as np

from ralgo.exceptions import DecodeError
from ralgo.utils import clean_depth, clean_bits, decode_binary, clean_chars


class Decoder:
    message: str
    chars: tuple
    depth: int
    bits: int

    parts: list
    output: str

    @staticmethod
    def __eval_bytes(content: str) -> Union[str, bytes]:
        try:
            if (content.startswith('b"') and content.endswith('"')) or (
                content.startswith("b'") and content.endswith("'")
            ):
                return ast.literal_eval(content)
            return content
        except Exception:  # pylint: disable=broad-except
            return content

    def __get_depth(self) -> int:
        depth = 0

        while self.message[depth] == self.chars[0]:
            depth += 1

        return depth

    def __get_bits(self) -> int:
        bits = 0

        while self.message[self.depth + bits] == self.chars[1]:
            bits += 1

        return bits

    def __cut_message(self) -> None:
        to_cut = self.depth + (self.bits * 2) + 1
        self.message = self.message[to_cut:]
        self.parts = re.findall("." * (self.bits + 1), self.message)

    def __fill_words(self) -> list[list]:
        words, word = [[]], 0
        self.output = ""

        for part in self.parts:
            if (
                part
                == self.chars[1]
                + (self.chars[0] * (self.bits - 1))
                + self.chars[1]
            ):
                word += 1
                words.append([])
            else:
                words[word].append(part)

        return words[:-1]

    def __fill_layers(self, word: list[str]) -> np.ndarray:
        layers = [[]]
        i = 0

        for element in word:
            if element[0] != self.chars[1]:
                layers[i].append(element)
            else:
                layers.append([])
                i += 1

        return np.array(layers[:-1]).T

    def __convert_layer(self, layers: np.ndarray) -> None:
        for i, layer in enumerate(layers):
            if len(layer) == self.depth:
                for j, element in enumerate(layer):
                    layers[i][j] = decode_binary(element, self.chars)
                self.output += chr(int(np.prod(layer.astype(int))))
            else:
                raise DecodeError(message="Failed to decode one layer")

    def decode(
        self,
        message: Union[str, bytes],
        chars: tuple,
        depth: int,
        bits: int,
    ) -> str:
        self.message = message
        self.chars = clean_chars(chars)

        self.depth = clean_depth(depth, self.__get_depth())
        self.bits = clean_bits(bits, self.__get_bits())

        self.__cut_message()

        for word in self.__fill_words():
            self.__convert_layer(self.__fill_layers(word))
            self.output += " "

        return self.__eval_bytes(self.output.strip())
