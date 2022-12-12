from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Hashset
    Time Complexity: O(m+n) = 3(m+n)
    Space Complexity: O(m+n)
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "findDifference",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums1=[1, 2, 3], nums2=[2, 4, 6]) == [[1, 3], [4, 6]]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]) == [[3], []]
