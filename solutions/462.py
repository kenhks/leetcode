from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Median
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(i - median) for i in nums)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minMoves2",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 10, 2, 9]) == 16


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(nums=[1, 2, 7]) == 6
