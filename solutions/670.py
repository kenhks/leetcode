from functools import reduce

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Comparision with sorted digits
    Time Complexity: O(log(10, n)) = 4log(10, n)
    Space Complexity: O(log(10, n))
    """

    def maximumSwap(self, num: int) -> int:
        digits = []
        while num > 0:
            num, d = divmod(num, 10)
            digits.append(d)
        digits = digits[::-1]
        sorted_digits = sorted(digits, reverse=True)
        for i in range(len(digits)):
            if digits[i] != sorted_digits[i]:
                for j in range(len(digits) - 1, i, -1):
                    if digits[j] == sorted_digits[i]:
                        swap_index = j
                        break
                digits[swap_index], digits[i] = digits[i], sorted_digits[i]
                break
        return reduce(lambda x, y: x * 10 + y, digits)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumSwap",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(num=2736) == 7236


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(num=9973) == 9973
