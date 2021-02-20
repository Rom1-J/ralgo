class Compress:
    message: str

    parts: list
    output: str

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
        return ''.join(str(i) for i in self.parts)

    def compress(self, message: str) -> str:
        self.message = message

        self.__fill_parts()

        return self.__gen_output()
