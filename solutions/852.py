from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Linear Scan
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak = -1
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                peak = i - 1
                break
        return peak


class Solution2:
    """
    Binary Search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "peakIndexInMountainArray",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([0, 1, 0]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([0, 2, 1, 0]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([0, 10, 5, 2]) == 1


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    assert solution([3, 4, 5, 1]) == 2


@pytest.mark.parametrize("solution", solutions)
def test_5(solution):
    assert solution([18, 29, 38, 59, 98, 100, 99, 98, 90]) == 5
