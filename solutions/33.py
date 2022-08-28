from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Find rotate count and binary search by part
    Time Complexity: O(n) = n + 2log(2, n)
    Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        rotate = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rotate = i
                break

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        return max(binary_search(0, rotate), binary_search(rotate + 1, len(nums) - 1))


class Solution2:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "search",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([4, 5, 6, 7, 0, 1, 2], 0) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([4, 5, 6, 7, 0, 1, 2], 3) == -1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([1, 3, 5], 0) == -1


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([3, 1], 1) == 1
