class RalgoException(Exception):
    """Base exception class for Ralgo"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class DepthError(RalgoException):
    """Exception that is thrown when given depth value is too low."""

    message: str


class BitsError(RalgoException):
    """Exception that is thrown when given bits value is too low."""

    message: str


class DecodeError(RalgoException):
    """Exception that is thrown when an error occurred during decode."""

    message: str


class DecompressParseError(RalgoException):
    """Exception that is thrown when an error occurred during parsing
    of compressed ralgo."""

    message: str


class InvalidArgument(RalgoException):
    """Exception that is thrown when an invalid type is passed to Ralgo."""

    message: str


class InvalidImage(RalgoException):
    """Exception that is thrown when an invalid image is passed to decode."""

    message: str
