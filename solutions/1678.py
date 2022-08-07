import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in replace()

    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = 3n
    """

    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


class Solution2:
    """
    Time Complexity: O(n) = n
    Space Complexity: O(n) = n
    """

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
                elif command[i + 1 : i + 4] == "al)":
                    real_cmd += "al"
                    i += 4
            else:
                real_cmd += "G"
                i += 1
        return real_cmd


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "interpret",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("G()(al)") == "Goal"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("G()()()()(al)") == "Gooooal"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("(al)G(al)()()G") == "alGalooG"
