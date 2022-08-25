from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
        return left


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "searchInsert",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 3, 5, 6], 5) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 3, 5, 6], 2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 3, 5, 6], 7) == 4
