from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Iterative
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        r2, r1_with_first = 0, 0
        for n in nums[:-1]:
            r2, r1_with_first = r1_with_first, max(n + r2, r1_with_first)
        r2, r1_without_first = 0, 0
        for n in nums[1:]:
            r2, r1_without_first = r1_without_first, max(n + r2, r1_without_first)
        return max(r1_with_first, r1_without_first)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "rob",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 3, 2]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2, 3, 1]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 2, 3]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1]) == 1
