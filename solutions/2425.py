from functools import reduce
from operator import xor
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(mn)
    Space Complexity: O(1)
    m = len(nums1), n = len(nums2)
    """

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in nums1:
            for j in nums2:
                ans ^= i ^ j
        return ans


class Solution2:
    """
    Bitwise Inverse count
    Time Complexity: O(m+n)
    Space Complexity: O(1)
    m = len(nums1), n = len(nums2)
    """

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return xor(
            len(nums1) % 2 * reduce(xor, nums2),
            len(nums2) % 2 * reduce(xor, nums1),
        )


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
    ],
    "xorAllNums",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]) == 13


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums1=[1, 2], nums2=[3, 4]) == 0
