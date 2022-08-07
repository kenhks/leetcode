import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-it lower()
    Time Complexity: O(n) = n
    Space Complexity: O(n) = n
    """

    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution2:
    """
    Use ASCII value
    Time Complexity: O(n) = n
    Space Complexity: O(n) = n
    """

    def toLowerCase(self, s: str) -> str:
        lower_s = ""
        A_ord, Z_ord = ord("A"), ord("Z")
        for char in s:
            if A_ord <= ord(char) <= Z_ord:
                lower_s += chr(ord(char) + 32)
            else:
                lower_s += char
        return lower_s


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "toLowerCase",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("Hello") == "hello"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("here") == "here"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("LOVELY") == "lovely"
