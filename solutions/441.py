import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        row = 0
        i = 1
        while n >= i:
            row += 1
            n -= i
            i += 1
        return row


class Solution2:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(0.25 + 2 * n) - 0.5))


class Solution3:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "arrangeCoins",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(5) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(8) == 3


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(15) == 5
