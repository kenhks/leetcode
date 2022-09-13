from functools import cache

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "climbStairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(3) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(5) == 8
