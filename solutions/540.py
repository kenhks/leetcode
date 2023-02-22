from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = -1
        for i in range(0, len(nums), 2):
            if i == (len(nums) - 1) or nums[i] != nums[i + 1]:
                ans = nums[i]
                break
        return ans


class Solution2:
    """
    Binary Search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "singleNonDuplicate",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([3, 3, 7, 7, 10, 11, 11]) == 10


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 1, 3]) == 3
