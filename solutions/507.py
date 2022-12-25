import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """

    def checkPerfectNumber(self, num: int) -> bool:
        sqrt = math.floor(math.sqrt(num))
        divisor_sum = 1 if num > 1 else 0
        for i in range(2, sqrt + 1):
            val, r = divmod(num, i)
            if r == 0:
                divisor_sum += i + val
        return divisor_sum == num


class Solution2:
    """
    Hard-Coded
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    ans = {6, 28, 496, 8128, 33550336}

    def checkPerfectNumber(self, num: int) -> bool:
        return num in self.ans


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "checkPerfectNumber",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(num=28)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(num=7)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(num=6)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution(num=496)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(num=8128)
