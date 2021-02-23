from typing import NoReturn, Union, Optional

from ralgo.exceptions import DepthError, BitsError, CharsError


def decode_binary(seq: str, replacements: tuple) -> int:
    """Decode binary

    Function used to parse a sequence as a binary following given
    replacements pattern

    Parameters
    ----------
    seq : str
        Sequence to decode
    replacements : tuple
        Pattern used in this sequence

    Returns
    -------
    int
       Evaluated decoded binary

    Example
    --------
    Using this function to decode ``,.,.,.`` with the pattern . and ,
    literal blocks::

        >>> decode_binary(",.,.,.", (".", ","))
        42
    """
    seq = seq.replace(replacements[0], "0").replace(replacements[1], "1")
    return int(seq, 2)


def encode_binary(seq: str, replacements: tuple) -> str:
    """Encode binary

    Function used to encode a binary to a sequence following given
    replacements pattern

    Parameters
    ----------
    seq : str
        Binary to encode
    replacements : tuple
        Pattern to use in the output sequence

    Returns
    -------
    int
       Generated sequence

    Example
    --------
    Using this function to encode ``101010`` with the pattern . and ,
    literal blocks::

        >>> encode_binary("101010", (".", ","))
        42
    """
    return seq.replace("0", replacements[0]).replace("1", replacements[1])


def clean_depth(
    depth: Optional[int],
    wanted_depth: int,
) -> Union[NoReturn, int]:
    """Clean depth

    Function used sort between given depth and auto generated depth

    Parameters
    ----------
    depth : Optional[int]
        Given depth
    wanted_depth : int
        Auto generated depth

    Returns
    -------
    Union[NoReturn, int]
       Selected depth
    """
    if depth:
        if not isinstance(depth, int):
            raise DepthError(message="Given depth must be an int")
        if wanted_depth > depth:
            raise DepthError(message="Given depth is too low")
        return depth

    return wanted_depth


def clean_chars(
    chars: tuple,
) -> Union[NoReturn, tuple]:
    """Clean chars

    Function used to check validity of given chars

    Parameters
    ----------
    chars : tuple
        Proposed chars

    Returns
    -------
    Union[NoReturn, tuple]
       Selected chars
    """
    if chars[0] == chars[1]:
        raise CharsError(message="Given chars must not be the same")
    return chars


def clean_bits(
    bits: Optional[int],
    wanted_bits: int,
) -> Union[NoReturn, int]:
    """Clean bits

    Function used sort between given bits and auto generated bits

    Parameters
    ----------
    bits : Optional[int]
        Given bits
    wanted_bits : int
        Auto generated bits

    Returns
    -------
    Union[NoReturn, int]
       Selected depth
    """
    if bits:
        if not isinstance(bits, int):
            raise BitsError(message="Given bits must be an int")
        if wanted_bits > bits:
            raise BitsError(message="Given bits is too low")
        return bits

    return wanted_bits
