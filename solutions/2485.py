import math

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two Pointer with prefix and suffix sum
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def pivotInteger(self, n: int) -> int:
        left = left_sum = 1
        right = right_sum = n
        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += left
            else:
                right -= 1
                right_sum += right
        return left if left_sum == right_sum else -1


class Solution2:
    """
    Math
    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) / 2
        ans = math.sqrt(total)
        return int(ans) if ans.is_integer() else -1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "pivotInteger",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(n=8) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(n=1) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(n=4) == -1
