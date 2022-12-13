from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Scan with max
    Time Complexity: O(n) = 2n
    Space Complexity: O(1)
    """

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(i + extraCandies) >= max_candies for i in candies]


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "kidsWithCandies",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(candies=[12, 1, 12], extraCandies=10) == [True, False, True]
