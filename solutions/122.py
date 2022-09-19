from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Greedy
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        return sum([j - i for i, j in zip(prices, prices[1:]) if j > i])


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxProfit",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([7, 1, 5, 3, 6, 4]) == 7


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 2, 3, 4, 5]) == 4


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([7, 6, 4, 3, 1]) == 0
