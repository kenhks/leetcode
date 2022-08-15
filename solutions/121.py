from typing import List

import pytest

from utils import parametrize_solution_cls


class Solution:
    """
    Brute Force
    Time Complexity: O(n^2) = (n) * (n - 1) / 2
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i, x in enumerate(prices):
            sell = max(prices[i + 1 :], default=-1)
            max_p = max(max_p, sell - x)
        return max_p


class Solution2:
    """
    Scan with two pointer
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            elif prices[r] >= prices[l]:
                max_p = max(max_p, prices[r] - prices[l])
                r += 1
        return max_p


class Solution3:
    """
    Scan with buy tracker
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0
        for _, x in enumerate(prices):
            if x < buy:
                buy = x
            elif x - buy > profit:
                profit = x - buy
        return profit


solutions = parametrize_solution_cls(
    [
        Solution,
        Solution2,
        Solution3,
    ],
    "maxProfit",
)


@pytest.mark.parametrize("solution", solutions)
def test_1(solution):
    assert solution([7, 1, 5, 3, 6, 4]) == 5


@pytest.mark.parametrize("solution", solutions)
def test_2(solution):
    assert solution([7, 6, 4, 3, 1]) == 0
