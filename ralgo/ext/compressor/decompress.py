from ralgo.exceptions import DecompressParseError


class Decompress:
    message: str

    parts: list

    def __fill_parts(self) -> None:
        self.parts = []
        tmp = ""
        enter = False

        for element in self.message:
            if element.isdigit():
                if not enter:
                    self.parts.append(int(element))
                else:
                    tmp += element
            elif element == "{":
                enter = True
            elif element == "}":
                enter = False
                self.parts.append(int(tmp))
                tmp = ""
            else:
                raise DecompressParseError(
                    message="Failed on parsing given compressed text",
                    expression=self.message,
                )

    def __gen_output(self) -> str:
        output = ""

        for i, part in enumerate(self.parts):
            if i % 2:
                output += "," * part
            else:
                output += "." * part

        return output

    def decompress(self, message: str) -> str:
        self.message = message

        self.__fill_parts()

        return self.__gen_output()
