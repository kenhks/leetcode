from itertools import zip_longest

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Calculate as written math
    Time Complexity: O(log(10, max(m, n))) = 2log(10, max(m, n)))
    Space Complexity: O(log(10, max(m, n)))
    m = len(num1), n = len(num2)
    """

    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = ""
        for d1, d2 in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            d1, d2 = int(d1), int(d2)
            carry, d = divmod(d1 + d2 + carry, 10)
            ans = str(d) + ans
        if carry:
            ans = "1" + ans
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "addStrings",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(num1="11", num2="123") == "134"


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(num1="456", num2="77") == "533"


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(num1="0", num2="0") == "0"
