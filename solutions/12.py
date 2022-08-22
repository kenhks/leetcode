import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashmap of value to symbol, order by value decreasingly
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    symbol_value = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def intToRoman(self, num: int) -> str:
        s = ""
        for digit_value, symbol in self.symbol_value.items():
            k, num = divmod(num, digit_value)
            s += symbol * k
        return s


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "intToRoman",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(3) == "III"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(58) == "LVIII"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1994) == "MCMXCIV"


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(24) == "XXIV"
