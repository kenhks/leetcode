from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return index


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "search",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([-1, 0, 3, 5, 9, 12], 9) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([-1, 0, 3, 5, 9, 12], 2) == -1
