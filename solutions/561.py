from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(n)
    """

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "arrayPairSum",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 4, 3, 2]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[6, 2, 6, 5, 1, 2]) == 9
