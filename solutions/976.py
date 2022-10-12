from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort by desending and check for triangle equality
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(1)
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "largestPerimeter",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 1, 2]) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2, 1]) == 0
