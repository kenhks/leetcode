from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Greedy with sorting
    Time Complexity: O(nlog(2, n)) = nlog(2, n) + n
    Space Complexity: O(1)
    """

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins >= c:
                ans += 1
                coins -= c
        return ans


solutions = parametrize_solution_cls(
    [
        Solution,
    ],
    "maxIceCream",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution(costs=[1, 3, 2, 4, 1], coins=7) == 4


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution(costs=[1, 6, 3, 1, 2, 5], coins=20) == 6
