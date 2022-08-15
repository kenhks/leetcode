from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maximumWealth",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([[1,2,3],[3,2,1]]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([[1,5],[7,3],[3,5]]) == 10


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([[2,8,7],[7,1,3],[1,9,5]]) == 17
