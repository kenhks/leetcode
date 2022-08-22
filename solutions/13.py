import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    replace subtract symbol then sum with hashmap
    Time Complexity: O(n) = 6n + n
    Space Complexity: O(1)
    """

    digit_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    subtract_replace = {
        "IV": "IIII",
        "IX": "VIIII",
        "XL": "XXXX",
        "XC": "LXXXX",
        "CD": "CCCC",
        "CM": "DCCCC",
    }

    def romanToInt(self, s: str) -> int:
        for i, j in self.subtract_replace.items():
            s = s.replace(i, j)
        s_sum = 0
        for i in s:
            s_sum += self.digit_value[i]
        return s_sum


class Solution2:
    """
    Use two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    digit_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        prev_c_value = s_int = self.digit_value[s[0]]
        for c in s[1:]:
            c_value = self.digit_value[c]
            if prev_c_value < c_value:
                s_int += c_value - 2 * prev_c_value
            else:
                s_int += c_value
            prev_c_value = c_value
        return s_int


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "romanToInt",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution("III") == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution("LVIII") == 58


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution("MCMXCIV") == 1994


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution("XXIV") == 24
