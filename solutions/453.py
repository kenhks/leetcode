from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Math
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def minMoves(self, nums: List[int]) -> int:
        n_min = float("inf")
        n_sum = 0
        for n in nums:
            n_min = min(n_min, n)
            n_sum += n
        return n_sum - n_min * len(nums)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "minMoves",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(nums=[1, 2, 3]) == 3


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(nums=[1, 1, 1]) == 0
