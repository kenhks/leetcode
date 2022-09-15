from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force with hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        i = 1
        while k > 0:
            if i not in seen:
                k -= 1
            i += 1
        return i - 1


class Solution2:
    """
    Sum index difference
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        i = 1
        while k > 0:
            if i not in seen:
                k -= 1
            i += 1
        return i - 1


class Solution3:
    """
    Binary search
    Time Complexity: O(log(2, n))
    Space Complexity: O(1)
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        shift = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) < k:
                shift = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return k + shift


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "findKthPositive",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([2, 3, 4, 7, 11], k=5) == 9


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2, 3, 4], 2) == 6
