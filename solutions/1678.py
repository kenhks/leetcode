class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


class Solution2:
    def interpret(self, command: str) -> str:
        size = len(command)
        i = 0
        real_cmd = ""
        while i < size:
            char = command[i]
            if char == "(":
                if command[i + 1] == ")":
                    real_cmd += "o"
                    i += 2
                elif command[i + 1: i + 4] == "al)":
                    real_cmd += "al"
                    i += 4
            else:
                real_cmd += "G"
                i += 1
        return real_cmd
        



def test_1():
    assert Solution().interpret("G()(al)") == "Goal"


def test_2():
    assert Solution().interpret("G()()()()(al)") == "Gooooal"


def test_3():
    assert Solution().interpret("(al)G(al)()()G") == "alGalooG"


def test_4():
    assert Solution2().interpret("G()(al)") == "Goal"


def test_5():
    assert Solution2().interpret("G()()()()(al)") == "Gooooal"


def test_6():
    assert Solution2().interpret("(al)G(al)()()G") == "alGalooG"