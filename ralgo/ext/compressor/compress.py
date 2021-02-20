class Compress:
    message: str

    parts: list

    def __fill_parts(self) -> None:
        self.parts = [1]

        last = self.message[0]
        i = 1

        while i < len(self.message):
            if self.message[i] == last:
                self.parts[-1] += 1
            else:
                self.parts.append(1)

            last = self.message[i]
            i += 1

    def __gen_output(self) -> str:
        output = ""

        for part in self.parts:
            if part < 10:
                output += str(part)
            else:
                output += f"{{{part}}}"

        return output

    def compress(self, message: str) -> str:
        self.message = message

        self.__fill_parts()

        return self.__gen_output()
