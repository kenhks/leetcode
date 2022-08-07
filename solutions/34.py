from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Linear Search
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> int:
        start, end = -1, -1
        if (not nums) or target < nums[0] or target > nums[-1]:
            return [start, end]
        for i, x in enumerate(nums):
            if x == target:
                start = end = i
                break
        j = i + 1
        while j < len(nums):
            if nums[j] == target:
                end = j
            j += 1
        return [start, end]


class Solution2:
    """
    Binary Search then Linear Search
    Time Complexity: O(log(n)) = log(n) + m1 + m2, where m1, m2 < (n // 2)
    Space Complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> int:
        start, end = -1, -1
        if (not nums) or target < nums[0] or target > nums[-1]:
            return [start, end]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                start = end = m
                break
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        i = m - 1
        while i > -1:
            if nums[i] != target:
                break
            start = i
            i -= 1
        j = m + 1
        while j < len(nums):
            if nums[j] != target:
                break
            end = j
            j += 1
        return [start, end]


class Solution3:
    """
    Double Binary Search
    Time Complexity: O(log(n)) = 2log(n)
    Space Complexity: O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            result = -1
            if nums and target >= nums[0]:
                l, r = 0, len(nums) - 1
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        result = m
                    if nums[m] >= target:
                        r = m - 1
                    else:
                        l = m + 1
            return result

        def find_last():
            result = -1
            if nums and target <= nums[-1]:
                l, r = 0, len(nums) - 1
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] == target:
                        result = m
                    if nums[m] <= target:
                        l = m + 1
                    else:
                        r = m - 1
            return result

        return [find_first(), find_last()]


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "searchRange",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([5, 7, 7, 8, 8, 10], 8) == [3, 4]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([], 0) == [-1, -1]


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([1], 1) == [0, 0]


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution([2, 2], 2) == [0, 1]


@pytest.mark.parametrize("solution", solutions)
def test_6(solution):
    assert solution([1, 1, 2], 1) == [0, 1]
