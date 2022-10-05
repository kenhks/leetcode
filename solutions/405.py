import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(log(16, n))
    Space Complexity: O(1)
    """

    def toHex(self, num: int) -> str:
        base = 16
        base_digits = "0123456789abcdef"
        hex_string = ""
        if num == 0:
            return "0"
        elif num < 0:
            num += 2**32
        while num:
            num, digit = divmod(num, base)
            hex_string = base_digits[digit] + hex_string
        return hex_string


class Solution2:
    """
    Bitwise Operation
    Time Complexity: O(log(16, n))
    Space Complexity: O(1)
    """

    def toHex(self, num: int) -> str:
        base_digits = "0123456789abcdef"
        hex_string = ""
        if num == 0:
            return "0"
        elif num < 0:
            num += 2**32
        while num:
            digit = num & 15
            num >>= 4
            hex_string = base_digits[digit] + hex_string
        return hex_string


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "toHex",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(26) == "1a"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(-1) == "ffffffff"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(15) == "f"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(0) == "0"
