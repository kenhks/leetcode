from functools import cache
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursion with Memorization
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_amount(i: int) -> int:
            if i < 0:
                return 0
            elif i <= 1:
                return nums[i]
            else:
                return nums[i] + max(rob_amount(i - 2), rob_amount(i - 3))

        return max(rob_amount(len(nums) - 1), rob_amount(len(nums) - 2))


class Solution2:
    """
    Iterative
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def rob(self, nums: List[int]) -> int:
        r2 = r1 = 0
        for n in nums:
            r2, r1 = r1, max(n + r2, r1)
        return r1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "rob",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 2, 3, 1]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([2, 7, 9, 3, 1]) == 12
