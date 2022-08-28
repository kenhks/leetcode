from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Find rotate count
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        rotate = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rotate = i + 1
                break
        if rotate:
            return min(nums[0], nums[rotate])
        else:
            return nums[0]


class Solution2:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                result = nums[mid + 1]
                break
            if nums[mid - 1] > nums[mid]:
                result = nums[mid]
                break
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return result


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "findMin",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 4, 5, 1, 2]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 5, 6, 7, 0, 1, 2]) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([11, 13, 15, 17]) == 11


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution([2, 1]) == 1
