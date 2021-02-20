def decode_binary(seq: str, replacements: tuple) -> int:
    seq = seq.replace(replacements[0], "0").replace(replacements[1], "1")
    return int(seq, 2)


def encode_binary(seq: str, replacements: tuple) -> str:
    return seq.replace("0", replacements[0]).replace("1", replacements[1])
