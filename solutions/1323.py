from functools import reduce

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Calculate digit values
    Time Complexity: O(log(10, n)) = 2log(10, n)
    Space Complexity: O(log(10, n))
    """

    def maximum69Number(self, num: int) -> int:
        digits = []
        while num:
            num, d = divmod(num, 10)
            digits.append(d)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 6:
                digits[i] = 9
                break
        return reduce(lambda x, y: 10 * x + y, digits[::-1], 0)


class Solution2:
    """
    Convert to string and replace
    Time Complexity: O(log(10, n)) = 3log(10, n)
    Space Complexity: O(log(10, n))
    """

    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "maximum69Number",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(9669) == 9969


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(9996) == 9999


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(9999) == 9999
