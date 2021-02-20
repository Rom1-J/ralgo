class RalgoException(Exception):
    """Base exception class for Ralgo"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class DepthError(RalgoException):
    """Exception that is thrown when given depth value is too low."""

    def __init__(self, expression: str = "", message: str = ""):
        super().__init__(message)

        self.expression = expression
        self.message = message


class BitsError(RalgoException):
    """Exception that is thrown when given bits value is too low."""

    def __init__(self, expression: str = "", message: str = ""):
        super().__init__(message)

        self.expression = expression
        self.message = message
