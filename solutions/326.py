import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Python built-in math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            return math.log(n, 3).is_integer()
        else:
            return False


class Solution2:
    """
    Recursive
    Time Complexity: O(log(3, n))
    Space Complexity: O(1)
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            return self.isPowerOfThree(n / 3)


class Solution3:
    """
    Iterative
    Time Complexity: O(log(3, n))
    Space Complexity: O(1)
    """

    def isPowerOfThree(self, n: int) -> bool:
        while n > 3:
            n = n // 3
        return n > 0 and (n == 3 or n == 1)


class Solution4:
    """
    Math, use max power of 3 is 3^19 over b^(log(b, 2^31-1)) for b = 3
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


class Solution5:
    """
    Pre-calculated hashmap
    Time Complexity: O(k)
    Space Complexity: O(k)
    k = (the max power of 3 < 32-bit signed int) + 1
    """

    power3set = {
        1,
        3,
        9,
        27,
        81,
        243,
        729,
        2187,
        6561,
        19683,
        59049,
        177147,
        531441,
        1594323,
        4782969,
        14348907,
        43046721,
        129140163,
        387420489,
        1162261467,
    }  # set(3**i for i in range(math.floor(math.log(2**31 - 1, 3)) + 1))

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and n in self.power3set


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
        Solution4,
        Solution5,
    ],
    "isPowerOfThree",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(27)


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert not solution(0)


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(9)


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert not solution(-1)


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution(1162261467)
