from typing import List
import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Time Complexity:
    Space Complexity:
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "intersection",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert sorted(solution(nums1, nums2)) == [2]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert sorted(solution(nums1, nums2)) == [4, 9]
