from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force with optimization
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        distance = 0
        for i, n1 in enumerate(nums1):
            j = len(nums2) - 1
            while i < j:
                if n1 <= nums2[j]:
                    distance = max(distance, j - i)
                    break
                j -= 1
            if (len(nums2) - i) <= distance:
                break
        return distance


class Solution2:
    """
    Binary search on second list
    Time Complexity: O(m log(2, n))
    Space Complexity: O(1)
    """

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        distance = 0
        for i, n1 in enumerate(nums1):
            left, right = i + 1, len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] < n1:
                    right = mid - 1
                else:
                    left = mid + 1
            distance = max(distance, left - i - 1)
            if (len(nums2) - i) <= distance:
                break
        return distance


class Solution3:
    """
    Two Pointer
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            while j < n and nums1[i] <= nums2[j]:
                j += 1
            res = max(res, j - i - 1)
            i += 1
        return res


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "maxDistance",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    assert solution(nums1, nums2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums1 = [2, 2, 2]
    nums2 = [10, 10, 1]
    assert solution(nums1, nums2) == 1


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    nums1 = [30, 29, 19, 5]
    nums2 = [25, 25, 25, 25, 25]
    assert solution(nums1, nums2) == 2


@pytest.mark.parametrize("solution", solutions)
def test_4(solution):
    nums1 = [
        9914,
        9434,
        8808,
        8041,
        7548,
        6727,
        5637,
        4635,
        2937,
        607,
        384,
        335,
    ]
    nums2 = [
        9980,
        9826,
        9620,
        9600,
        9455,
        9448,
        9374,
        9367,
        9278,
        9251,
        9083,
        8987,
        8952,
        8932,
        8762,
        8705,
        8595,
        8460,
    ]
    assert solution(nums1, nums2) == 14
