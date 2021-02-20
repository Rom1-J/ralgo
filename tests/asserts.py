def contains_only(text: str, chars: tuple) -> bool:
    return all((letter in chars) for letter in text)
