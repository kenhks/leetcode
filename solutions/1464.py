from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Sort desecnding
    Time Complexity: O(nlog(2, n))
    Space Complexity: O(n)
    """

    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxProduct",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([3, 4, 5, 2]) == 12


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 5, 4, 5]) == 16


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([3, 7]) == 12
