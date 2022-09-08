from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Calculate cumulative sum from right and left
    Time Complexity: O(n) = 2n
    Space Complexity: O(n) = 2n
    """

    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        right_cumsum = [0] * (len(nums) + 1)
        for j in range(len(nums) - 1, -1, -1):
            right_cumsum[j] = nums[j] + right_cumsum[j + 1]
        left_cumsum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            left_cumsum[i + 1] = left_cumsum[i] + nums[i]
            if left_cumsum[i] == right_cumsum[i + 1]:
                index = i
                break
        return index


class Solution2:
    """
    Calculate total and check difference
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cumsum = 0
        index = -1
        for i in range(len(nums)):
            total -= nums[i]
            if cumsum == total:
                index = i
                break
            cumsum += nums[i]
        return index


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "pivotIndex",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 7, 3, 6, 5, 6]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2, 3]) == -1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([2, 1, -1]) == 0
