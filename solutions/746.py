from functools import cache
from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Recursive with Memorization
    Time Complexity: O(n!) = n + 1
    Space Complexity: O(n) = n
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def min_cost(i):
            if i >= 2:
                return cost[i] + min(min_cost(i - 1), min_cost(i - 2))
            else:
                return cost[i]

        size = len(cost)
        return min(min_cost(size - 1), min_cost(size - 2))


class Solution2:
    """
    Iterative with hashmap
    Time Complexity: O(n) = n + 1
    Space Complexity: O(n) = n + 2
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_map = {-1: 0, -2: 0}
        for i, x in enumerate(cost):
            cost_map[i] = x + min(cost_map[i - 1], cost_map[i - 2])
        return min(cost_map[len(cost) - 1], cost_map[len(cost) - 2])


class Solution3:
    """
    Iterative with two pointer
    Time Complexity: O(n) = n + 1
    Space Complexity: O(k) = 3
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p2 = p1 = 0
        for x in cost:
            i_cost = x + min(p2, p1)
            p2, p1 = p1, i_cost
        return min(p2, p1)


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "minCostClimbingStairs",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([10, 15, 20]) == 15


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


@pytest.mark.parametrize("solution", solutions)
def test_3(solution):
    assert solution([10, 20]) == 10
