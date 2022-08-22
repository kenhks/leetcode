import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            return math.log(n, 4).is_integer()
        else:
            return False


class Solution2:
    """
    Recursive
    Time Complexity: O(log(4, n))
    Space Complexity: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            return self.isPowerOfFour(n / 4)


class Solution3:
    """
    Iterative
    Time Complexity: O(log(4, n))
    Space Complexity: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        while n > 4:
            n /= 4
        return n > 0 and (n == 4 or n == 1)


class Solution4:
    """
    Bit manipulation
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0) and ((n & (n - 1)) == 0) and ((n & 0xAAAAAAAA) == 0)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
        Solution4,
    ],
    "isPowerOfFour",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(16)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(5)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(1)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(-1)
