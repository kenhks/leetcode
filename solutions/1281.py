from functools import reduce

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in Conversion int str
    Time Complexity: O(log(10, n)) = 4 log(10, n)
    Space Complexity: O(log(10, n))
    """

    def subtractProductAndSum(self, n: int) -> int:
        str_n = [int(i) for i in str(n)]
        return reduce(lambda x, y: x * y, str_n) - sum(str_n)


class Solution2:
    """
    Calculate over digit value
    Time Complexity: O(log(10, n)) = log(10, n)
    Space Complexity: O(1)
    """

    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        while n > 0:
            digit_value = n % 10
            sum += digit_value
            product *= digit_value
            n = n // 10
        return product - sum


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "subtractProductAndSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(234) == 15


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(4421) == 21
