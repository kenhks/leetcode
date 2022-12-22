from functools import cache

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """

    @cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "get_anagram_period",
)


@pytest.mark.parametrize("solution", solutions)
def test_1():
    assert Solution().fib(2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2():
    assert Solution().fib(3) == 2


@pytest.mark.parametrize("solution", solutions)
def test_3():
    assert Solution().fib(4) == 3
