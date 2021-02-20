from typing import NoReturn, Union

from ralgo.exceptions import DepthError, BitsError


def decode_binary(seq: str, replacements: tuple) -> int:
    seq = seq.replace(replacements[0], "0").replace(replacements[1], "1")
    return int(seq, 2)


def encode_binary(seq: str, replacements: tuple) -> str:
    return seq.replace("0", replacements[0]).replace("1", replacements[1])


def clean_depth(
    depth: Union[None, int],  # pylint: disable=unsubscriptable-object
    wanted_depth: int,
) -> Union[NoReturn, int]:  # pylint: disable=unsubscriptable-object
    if depth:
        if not isinstance(depth, int):
            raise DepthError(message="Given depth must be an int")
        if wanted_depth > depth:
            raise DepthError(message="Given depth is too low")
        return depth

    return wanted_depth


def clean_bits(
    bits: Union[None, int],  # pylint: disable=unsubscriptable-object
    wanted_bits: int,
) -> Union[NoReturn, int]:  # pylint: disable=unsubscriptable-object
    if bits:
        if not isinstance(bits, int):
            raise BitsError(message="Given bits must be an int")
        if wanted_bits > bits:
            raise BitsError(message="Given bits is too low")
        return bits

    return wanted_bits
